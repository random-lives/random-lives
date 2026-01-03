import numpy as np
from scipy.interpolate import CubicSpline, interp1d

class Raw_Data:
    def __init__(self, name, xs, ys):  
        self.name = name
        self.min_x = np.min(xs)
        self.max_x = np.max(xs)
        self.years = np.arange(self.min_x,self.max_x)
        
        self.xs    = np.array(xs)
        self.ys    = np.array(ys)
        self.pop = lambda x : np.exp(interp1d(self.xs,np.log(self.ys+1),fill_value='extrapolate')(x))-1

        self.birth_data  = False
        self.cbr_data    = False
        self.LE_data     = False
        
        self.hyde_id     = None
        self.lifetable   = "General"

    def add_births(self, birth_xs, birth_ys):
        self.birth_data  = True
        
        self.birth_xs    = np.array(birth_xs)
        self.birth_ys    = np.array(birth_ys)

        self.birth = lambda x : np.exp(interp1d(self.birth_xs,np.log(self.birth_ys+1),fill_value='extrapolate')(x))-1

    def add_LE(self, LE_xs, LE_ys):
        self.LE_data  = True

        sort_indices = np.argsort(np.array(LE_xs))
        self.LE_xs    = np.array(LE_xs)[sort_indices]
        self.LE_ys    = np.array(LE_ys)[sort_indices]

        self.LE = interp1d(self.LE_xs,self.LE_ys,fill_value='extrapolate')

    def add_cbr(self, cbr_xs, cbr_ys):
        self.cbr_data  = True
        
        self.cbr_xs    = np.array(cbr_xs)
        self.cbr_ys    = np.array(cbr_ys)

        self.cbr = interp1d(self.cbr_xs,self.cbr_ys,fill_value='extrapolate')

country_data_years = np.concatenate(([1600],np.arange(1700,1950,10),np.arange(1950,2026)))

class Country_Data:
    def __init__(self, country, LE_1600 = 25, cbr_1600 = 45):
        self.hyde_id   = country.hyde_id
        self.lifetable = country.lifetable
        self.years = country_data_years
        
        self.pop_data = country.pop(self.years)

        #extrapolating births
        vec_1950 = np.arange(1950,2026)
        births_1950 = country.birth(vec_1950)

        vec_1800 = np.arange(1800,1950)
        births_1800 = country.cbr(vec_1800)*country.pop(vec_1800)/1e3

        vec_1600 = np.arange(1600,1800)
        cbr_intr = cbr_1600 + (vec_1600-1600)/200*(country.cbr_ys[0]-cbr_1600)
        births_1600 = cbr_intr*country.pop(vec_1600)/1e3

        births_vec = np.concatenate((births_1600,births_1800,births_1950))
        self.birth_data = interp1d(np.arange(1600,2026),births_vec,fill_value='extrapolate')(country_data_years)

        # calculate cbr from births
        self.CBR_data = 1e3*self.birth_data/self.pop_data

        # extrapolating life expectancy
        LE_intr = LE_1600 + (vec_1600-1600)/200*(country.LE_ys[0]-LE_1600)
        LE_concat_xs = np.concatenate((vec_1600, country.LE_xs))
        LE_concat_ys = np.concatenate((LE_intr,  country.LE_ys))
        self.LE_data = interp1d(LE_concat_xs,LE_concat_ys,fill_value='extrapolate')(country_data_years)

        self.pop_f    = lambda x : np.exp(interp1d(self.years,np.log(self.pop_data+1))(x))-1
        self.birth_f  = lambda x : np.exp(interp1d(self.years,np.log(self.birth_data+1))(x))-1
        self.CBR_f = interp1d(self.years,self.CBR_data)
        self.LE_f  = interp1d(self.years,self.LE_data)