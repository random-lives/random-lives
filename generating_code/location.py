"""Location utilities for geographic data lookup.

This module handles conversion from HYDE grid coordinates to geographic
information including country, region, biome, climate, and detailed addresses.
"""

# Suppress GDAL warnings before importing geopandas (which triggers them on import)
import warnings
warnings.filterwarnings('ignore', message='Cannot find header.dxf')
warnings.filterwarnings('ignore', message='Cannot set the CRS')
warnings.filterwarnings('ignore', category=RuntimeWarning, module='pyogrio')

import csv
import numpy as np
import rasterio
import requests
from PIL import Image
import geopandas as gpd
from shapely.geometry import Point

# =============================================================================
# Lazy Load Geographic Data
# =============================================================================

# Module-level cache variables (loaded on first use)
_data_loaded = False
_iso_data = None
_sub_iso_data = None
_max_land_area = None
_total_area = None
_ID_to_country = None
_Subregion_ID = None
_ecoregions = None
_elevation = None
_clim_maps = None

_biome_names = {
    1: 'Tropical & Subtropical Moist Broadleaf Forests',
    2: 'Tropical & Subtropical Dry Broadleaf Forests',
    3: 'Tropical & Subtropical Coniferous Forests',
    4: 'Temperate Broadleaf & Mixed Forests',
    5: 'Temperate Conifer Forests',
    6: 'Boreal Forests/Taiga',
    7: 'Tropical & Subtropical Grasslands, Savannas & Shrublands',
    8: 'Temperate Grasslands, Savannas & Shrublands',
    9: 'Flooded Grasslands & Savannas',
    10: 'Montane Grasslands & Shrublands',
    11: 'Tundra',
    12: 'Mediterranean Forests, Woodlands & Scrub',
    13: 'Deserts & Xeric Shrublands',
    14: 'Mangroves',
    98: 'Lake',
    99: 'Rock and Ice'
}

_clim_vars = {
    'bio_1': "Mean Temp",
    'bio_5': "Warmest Month Temp",
    'bio_6': "Coldest Month Temp",
    'bio_12': "Annual Precipitation",
}


def _ensure_data_loaded():
    """Load all geographic data files on first call. Subsequent calls are no-ops."""
    global _data_loaded, _iso_data, _sub_iso_data, _max_land_area, _total_area
    global _ID_to_country, _Subregion_ID, _ecoregions, _elevation, _clim_maps

    if _data_loaded:
        return

    # ISO country codes
    with rasterio.open('Raw_Data/HYDE34/general/iso_cr.asc') as src:
        _iso_data = src.read(1)

    # ISO subregion codes
    with open('Raw_Data/HYDE34/general/sub_iso_cr.asc', 'r') as f:
        ncols = int(f.readline().split()[1])
        nrows = int(f.readline().split()[1])
        xllcorner = float(f.readline().split()[1])
        yllcorner = float(f.readline().split()[1])
        cellsize = float(f.readline().split()[1])
        nodata = float(f.readline().split()[1])
        _sub_iso_data = np.loadtxt(f).reshape(nrows, ncols)

    # Land area data
    with rasterio.open('Raw_Data/HYDE34/general/maxln_cr.asc') as src:
        _max_land_area = src.read(1)
        _max_land_area = _max_land_area * (_max_land_area > 0)

    with rasterio.open('Raw_Data/HYDE34/general/garea_cr.asc') as src:
        _total_area = src.read(1)
        _total_area = _total_area * (_max_land_area > 0)

    # Country ID mapping (loaded from processed data)
    import dill
    with open('Processed_Data/processed_p1600_data.pkl', 'rb') as f:
        _country_data = dill.load(f)

    _ID_to_country = {-9999: 'None'}
    for name in _country_data:
        _ID_to_country[_country_data[name].hyde_id] = name

    # Subregion ID mapping
    _Subregion_ID = {}
    with open('Raw_Data/HYDE34/general/region_key.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            _Subregion_ID[int(row[1])] = row[5]
    _Subregion_ID[-9999] = None

    # Biome data
    _ecoregions = gpd.read_file('Raw_Data/Geography/wwf_eco/wwf_terr_ecos.shp')

    # Climate data
    _elevation = np.array(Image.open('Raw_Data/Geography/climatology/wc2.1_5m_elev.tif'))

    _clim_maps = {}
    for var in _clim_vars:
        _clim_maps[var] = np.array(Image.open(f'Raw_Data/Geography/climatology/wc2.1_5m_{var}.tif'))

    _data_loaded = True


# =============================================================================
# Helper Functions
# =============================================================================

def get_biome(lat, lon):
    """Query biome and ecoregion for a coordinate."""
    _ensure_data_loaded()
    point = Point(lon, lat)
    matches = _ecoregions[_ecoregions.contains(point)]

    if len(matches) == 0:
        return None, None

    biome_code = matches.iloc[0]['BIOME']
    biome_name = _biome_names.get(biome_code, 'Unknown')
    eco_name = matches.iloc[0]['ECO_NAME']

    return biome_name, eco_name


def get_detailed_location(lat, lon):
    """Get detailed address from OpenStreetMap reverse geocoding."""
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'zoom': 14
    }
    headers = {'User-Agent': 'RandomLives'}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        return data.get('display_name')
    except Exception:
        return None


# =============================================================================
# Location Class
# =============================================================================

class Location:
    """Geographic location based on HYDE grid coordinates.

    Provides access to:
    - Coordinates (lat/lon)
    - Modern country and subregion
    - Detailed address (via OpenStreetMap)
    - Biome and ecoregion
    - Elevation and climate data
    """

    def __init__(self, row, col):
        _ensure_data_loaded()
        self.row = row
        self.col = col

        self.total_area = _total_area[self.row, self.col]
        self.land_area = _max_land_area[self.row, self.col]

        self._get_latlon()
        self._get_country()
        self._get_subregion()
        self._get_detailed_location()

    def _get_latlon(self):
        """Convert grid coordinates to lat/lon."""
        res = 0.0833  # 360/4320 degrees
        self.lon = round(-180 + (self.col + 0.5) * res, 2)
        self.lat = round(90 - (self.row + 0.5) * res, 2)

    def _get_country(self):
        """Look up modern country."""
        country_id = _iso_data[self.row, self.col]
        self.country = _ID_to_country.get(country_id, 'Unknown')

    def _get_subregion(self):
        """Look up modern subregion."""
        isocode = int(_sub_iso_data[self.row, self.col])
        self.subregion = _Subregion_ID.get(isocode, None)

    def _get_detailed_location(self):
        """Get detailed address via reverse geocoding."""
        self.address = get_detailed_location(self.lat, self.lon)

    def biome(self):
        """Return (biome_name, ecoregion_name) tuple."""
        return get_biome(self.lat, self.lon)

    def altitude(self):
        """Return elevation in meters."""
        _ensure_data_loaded()
        return _elevation[self.row, self.col]

    def climate(self):
        """Return dict of climate variables."""
        _ensure_data_loaded()
        output = {}
        for var in _clim_vars:
            output[_clim_vars[var]] = _clim_maps[var][self.row, self.col]
        return output

    def gmap_url(self, zoom=8):
        """Return Google Maps URL for this location.

        Args:
            zoom: Zoom level (1=world, 5=landmass/continent, 10=city, 15=streets, 20=buildings)
                  Default is 8 (regional view)
        """
        return f"https://www.google.com/maps/place/{self.lat},{self.lon}/@{self.lat},{self.lon},{zoom}z"

    def local_land_area(self, size):
        """Get total land area in a square around this cell."""
        grid = _max_land_area[
            self.row - size:self.row + size + 1,
            self.col - size:self.col + size + 1
        ]
        return np.sum(np.nan_to_num(grid))

    def p_print(self):
        """Pretty print location info."""
        print("Coordinates:", self.lat, 'N, ', self.lon, 'E')
        print("Modern Location:", self.subregion, ',', self.country)
        print("Modern Address:", self.address, '\n')
        print("Altitude:", self.altitude(), 'm')

        biome, ecotype = self.biome()
        print('Biome:', biome)
        print('Ecotype:', ecotype, '\n')

        clim_data = self.climate()
        for key in clim_data:
            print(key + ':', clim_data[key])
        print('')
        print(self.gmap_url())
