# Prosopography Database Access Audit

*Created 2026-06-21 11:42.*
*Last revised 2026-06-21 12:05 — merged four regional verification passes into one reconciled note.*

Verification of the online accessibility, access mode, and headline counts of the prosopographical / name databases cited in [named-individuals-premodern.md](named-individuals-premodern.md), for the "Name recorded anywhere" tier of [The Pyramid of Oblivion](pyramid-of-oblivion.md). Each resource is classified by whether its URL is live, how the data can be accessed, and whether its individual-count figure holds up.

## Summary

Of the ~30 resources checked, nearly all are live. Only one URL is outright dead — **OCIANA**'s old Oxford host (`krc.orient.ox.ac.uk/ociana/`), which relaunched as **OCIANA 2.0 at Ohio State** ([ociana.osu.edu](https://ociana.osu.edu/)) in September 2024 — and **PLRE** has no queryable online database at all (only page-image scans of the print volumes on Archive.org). Two access caveats: **BDTNS**'s `filol.csic.es` host has a broken TLS certificate, so use the clean CESGA mirror [bdtns.cesga.es](https://bdtns.cesga.es/); and **SNAP:DRGN**'s aggregated triplestore (once ~650,000 person-records) has expired and is now a standards project only, not a live dataset.

**Roughly 17 resources offer genuine bulk download or an API** usable for re-deriving counts — well above the "seven" a first single-pass audit found, because the regional checks proved that several databases the first pass marked search-only (PIR, LGPN, OCIANA) in fact publish downloadable data. The single most valuable source is **CBDB** — the largest pre-modern biographical database in the world (~650,000 individuals), fully downloadable as one SQLite file, so the pre-1500 subset can be computed exactly by querying birth/death years rather than guessed. Next most tractable for extraction: **Trismegistos** (~389,000 individuals, Egypt), **LGPN** (~400,000, Greek world), **EDH** (open, person-modeled Roman epigraphy), and the cuneiform corpus (CDLI + the Oracc/Prosobab/PNA prosopographies). The biggest figures to update in the note: **EDCS now holds ~542,000 inscriptions** (its 509,600 is from 2018) and **CDLI has crossed ~500,000 artifacts** (its ~320,000 is stale).

## Headline tally

- **Live:** ~28 of ~30. Dead/moved: OCIANA (old Oxford URL). No live DB yet: PLRE (print scans only).
- **Bulk-downloadable / API:** ~17 (see ranked list below).
- **Search-only / open-but-no-export:** BDTNS (full corpus), PHI, Persons of Ancient Athens, Porter & Moss, Onomasticon Arabicum, CIL, PBE, PASE, Online Catasto, MHD, Matrícula, Who's Who in Korean History, DASI (bot-shielded).
- **Paywalled:** ODNB (subscription / library access).
- **Print-only:** PLRE (page scans), Prosopographia Ptolemaica (folded into Trismegistos), Hatra (Marcato 2018), Meroitic/Old Nubian/Ge'ez onomastica.
- **Defunct:** SNAP:DRGN aggregated triplestore.

## Full table

Access mode key: **(a)** open + queryable web search; **(b)** bulk download / API; **(c)** search-only, no export; **(d)** paywalled; **(e)** print-only.

| Resource (region / period) | URL & host | Live? | Access | Distinct named individuals | Notes |
|---|---|---|---|---|---|
| **CDLI** — cuneiform artifacts, c.3350 BCE–1st m. BCE | [cdli.earth](https://cdli.earth/) (intl. consortium, formerly UCLA) | Yes | (a)+(b) | **N/A** — artifact catalogue, not a prosopography; ~500,000 artifacts (About page inconsistent, 360,000–400,000+) | Daily CSV/ATF dump [github.com/cdli-gh/data](https://github.com/cdli-gh/data) (git-lfs; automation possibly stale since 2022, live exports remain); CTS API [cdli-cts](https://github.com/cdli-gh/cdli-cts). Note's "~320,000" is stale. |
| **BDTNS** — Ur III, c.2100–2000 BCE | [bdtns.filol.csic.es](https://bdtns.filol.csic.es/) (broken cert) → mirror [bdtns.cesga.es](https://bdtns.cesga.es/) (CSIC + CESGA) | Yes (use mirror) | (a)/(c) | No individual count; **105,187 tablets** (May 2026; note's 104,923 is slightly stale) | Per-search export only; no advertised whole-corpus dump. |
| **PNA** — Neo-Assyrian, c.911–609 BCE | [oracc.museum.upenn.edu/pnao](https://oracc.museum.upenn.edu/pnao/) (Oracc / Penn) | Yes | (a)+(b) | **>25,000** (full printed PNA); 17,000 in the open social-network extract | Online portal serves addenda only, but the full data is in the Oracc JSON corpus [github.com/oracc/json](https://github.com/oracc/json) (`/projects.json` → `/pnao/manifest.json` → `corpusjson/`), **CC0**. SNA dataset: [Helsinki portal](https://researchportal.helsinki.fi/en/datasets/a-social-network-of-the-prosopography-of-the-neo-assyrian-empire), [Alstola et al. (2023)](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.74). |
| **Prosobab** — Neo-Babylonian/Achaemenid Babylonia, c.620–330 BCE | [prosobab.leidenuniv.nl](https://prosobab.leidenuniv.nl/) (Leiden) | Yes | (a)+(b) | **~21,000 persons** (confirms note) | Per-query Excel/CSV export plus full relational-DB dump: [Zenodo 6642356](https://zenodo.org/record/6642356) ([Waerzeggers & Groß (2022)](https://zenodo.org/record/6642356)). **CC BY-NC 4.0.** |
| **Trismegistos People** — Egypt + E. Mediterranean, 800 BCE–800 CE | [trismegistos.org/ref](https://www.trismegistos.org/ref/) (KU Leuven) | Yes | (a)+(b) | **388,901 individuals**; 568,999 attestations; 43,097 names (confirms note) | [Data Services](https://www.trismegistos.org/dataservices/): PerResponder JSON + PerRDF endpoints, **CC BY-SA 4.0**. Full person table-dumps reserved for institutional data packages. Homepage 403s to bots but renders in a browser. |
| **Porter & Moss** — pharaonic Egypt | [topbib.griffith.ox.ac.uk](https://topbib.griffith.ox.ac.uk/) (Griffith Inst., Oxford) | Yes (relaunched Jan 2026) | (a)/(c) | N/A — bibliography of monuments, not persons | Hierarchical DB + searchable PDFs of print vols 1–7; no data export. |
| **Prosopographia Ptolemaica** — Ptolemaic Egypt | [Digital Classicist wiki](https://wiki.digitalclassicist.org/Prosopographia_Ptolemaica) | Yes (wiki) | (e) | ~50,000 entries (confirms note) | Folded into Trismegistos; no standalone live DB. |
| **LGPN** — Greek world, 8th c. BCE–c.600 CE | [lgpn.ox.ac.uk](https://www.lgpn.ox.ac.uk/), search at [search.lgpn.ox.ac.uk](https://search.lgpn.ox.ac.uk) (Oxford / British Academy) | Yes | (a)+(b) | **~400,000** archive; 300,582 published online sharing 35,982 names (confirms note) | TEI/XML in eXist-db with an **OpenAPI/REST endpoint** (`clas-lgpn5.classics.ox.ac.uk:8080/exist/apps/lgpn-api/`, intermittently slow); dataset deposited at ORA ([uuid:c8d732d0…](https://ora.ox.ac.uk/objects/uuid:c8d732d0-05a1-40a2-9f18-92664e235720)). Attribution, non-commercial. |
| **PHI Greek Inscriptions** — Greek epigraphy | [inscriptions.packhum.org](https://inscriptions.packhum.org/) (Packard Humanities Inst.) | Yes | (c)/(d) | N/A — ~150,000 inscriptions, no person index | License forbids copying beyond personal fair use → no bulk export. Feeds LGPN. |
| **Persons of Ancient Athens** — Attica | [attica.artsci.utoronto.ca](https://attica.artsci.utoronto.ca/) (Toronto) | Yes | (a)/(c) | >100,000 entries (confirms note) | HTML search only; backed by the EMPRESS relational DB. Partly redundant with LGPN. |
| **EDH — Epigraphic Database Heidelberg** — Roman inscriptions | [edh.ub.uni-heidelberg.de](https://edh.ub.uni-heidelberg.de/) (Heidelberg Academy) | Yes | (a)+(b) | ~81,000 inscriptions; **explicitly models persons** (prosopography in RDF) | *Missed by the note.* Open Data Repository, **CC BY-SA 4.0**: CSV/JSON/SPARQL/EpiDoc + GeoJSON. ETL: [github.com/sdam-au/EDH_ETL](https://github.com/sdam-au/EDH_ETL). Cleanest open Roman dataset for a defensible distinct-person count. |
| **EDCS** — Latin/Greek inscriptions (Roman) | [db.edcs.eu](https://db.edcs.eu/epigr/epi.php) → [edcs.hist.uzh.ch](https://edcs.hist.uzh.ch/) (U. Zurich) | Yes | (a)/(b via scraper) | **~542,496 inscriptions** (up from note's 509,600); no distinct-person count | Search-only on site; **Lat-Epig** ([github.com/mqAncientHistory/Lat-Epig](https://github.com/mqAncientHistory/Lat-Epig)) scrapes results to TSV. ~170,000 images. Under renewal since 2024. |
| **CIL** — Latin inscriptions | [cil.bbaw.de](https://cil.bbaw.de/) (BBAW) | Yes | (a)/(c) | ~180,000 inscriptions (confirms note); no distinct-person count | Online "Datenbank ACE" + print volumes; no API/bulk. Person value is the print *indices nominum*. |
| **PIR** — Roman elite, 31 BCE–c.300 CE | [pir.bbaw.de](https://pir.bbaw.de/) (BBAW / TELOTA) | Yes | (a)+(b) | ~14,000–15,000 (confirms note) | **JSON REST API + CSV in/out** via open-source app [github.com/telota/PIR](https://github.com/telota/PIR) (GPLv3 code; data licence unstated). Online entries = name + citation only (biography redacted). |
| **PLRE** — Later Roman governing class, 260–641 CE | digitisation: [Connecting Late Antiquities / PLRBW](https://ics.sas.ac.uk/research/prosopography-later-roman-byzantine-worlds); scans on [Archive.org](https://archive.org/details/prosopography-later-roman-empire) | **No live DB** | (e) | "over 10,000" (confirms note) | Digital version in progress (began Feb 2023), intended for Cambridge Core, **not confirmed launched as of 6/2026**. Only page-image scans online. |
| **PBE** — Byzantine, 641–867 | [pbe.kcl.ac.uk](https://pbe.kcl.ac.uk/) (KCL) | Yes | (a)/(c) | "several thousand" (no published total) | PBE I online edition; no export. Seeded PBW. |
| **PmbZ** — mid-Byzantine, 641–1025 | [telota.bbaw.de/pmbz](https://telota.bbaw.de/pmbz/) (BBAW / De Gruyter) | Yes | (a)+(b) | **~21,500** (11,500 + 10,000; confirms note) | **Open-access full-text DB** (data released end-2017); De Gruyter edition also now open-access (was paywalled). No one-click dump, but fully readable/searchable. |
| **PBW** — Byzantine, 1025–1180s | [pbw2016.kdl.kcl.ac.uk](https://pbw2016.kdl.kcl.ac.uk/) (KCL / KDL) | Yes (behind anti-bot wall) | (a)/(b partial) | ~10,000 individuals, ~60,000 factoids (confirms note) | Factoid-model DB, LOD-oriented (unique person IDs; ontology [github.com/johnBradley501/FPO](https://github.com/johnBradley501/FPO)); open-source build [pbw-os.kdl.kcl.ac.uk](https://pbw-os.kdl.kcl.ac.uk/). No single advertised SQL/RDF dump found. |
| **PASE** — Anglo-Saxon England, 597–1100 | [pase.ac.uk](https://pase.ac.uk/) (moved to Oxford History Faculty, 2024) | Yes | (a)/(c) | **19,807** (PASE 2; confirms note) | Server move 2024 may have dropped KCL export endpoints; treat bulk as unconfirmed. |
| **OpenDomesday** — England, 1086 | [opendomesday.org](https://opendomesday.org/) (Powell-Smith; data Palmer / Hull) | Yes | (a)+(b) | 268,984 heads of household counted; named landholders ~low thousands (~1,400 tenants-in-chief) | **Public JSON API, no key**: [opendomesday.org/api/](https://opendomesday.org/api/) (manor/place/county/hundred). Raw data at U. Hull repository. No single distinct-person total. |
| **People of Medieval Scotland** — Scotland, 1093–1371 | [poms.ac.uk](https://www.poms.ac.uk/) (KCL / KDL) | Yes (behind anti-bot wall) | (a)+(b) | **~21,000** (confirms note) | Full dataset on KDL CKAN: [data.kdl.kcl.ac.uk/dataset/people-of-medieval-scotland-project-1093-1371](https://data.kdl.kcl.ac.uk/dataset/people-of-medieval-scotland-project-1093-1371), Creative Commons, RDF + API. |
| **Online Catasto of 1427** — Tuscany | [cds.library.brown.edu/projects/catasto](https://cds.library.brown.edu/projects/catasto/overview.html) (Brown) | Yes | (a)/(c) | ~260,000 individuals / ~60,000 households (confirms note) | Public web DB ≈10,000 city-of-Florence records; full Herlihy–Klapisch-Zuber file archived separately (historically ICPSR), not a download button. |
| **ODNB** — British lives, all periods | [oxforddnb.com](https://www.oxforddnb.com/) (OUP) | Yes | (d) | **60,000+** articles now (note's 50,113/54,922 is the 2004 print figure); **pre-1500 ≈ 5,000 "medieval lives"** | Subscription / library access; no bulk export. Pre-1500 share ≈ 9–10%, per [Summerson (2018)](https://blog.oup.com/2018/10/medieval-dictionary-national-biography/). |
| **Onomasticon Arabicum** — Islamic scholars/notables | [onomasticon.irht.cnrs.fr](https://onomasticon.irht.cnrs.fr/) (IRHT/CNRS) | Yes | (a)/(c) | ~27,000–28,000 online (confirms note); card archive holds 100,000+ | Bilingual search; no advertised data download/API. |
| **Princeton Geniza Project** — Cairo Geniza, c.950–1250 | [geniza.princeton.edu](https://geniza.princeton.edu/) (Princeton Geniza Lab / CDH) | Yes | (a)+(b) | **1,802 person records**; ~35,855 documents | *Missed by the note.* CSV exports [github.com/princetongenizalab/pgp-metadata](https://github.com/princetongenizalab/pgp-metadata) (people.csv, documents.csv, places.csv…) + transcriptions [pgp-text](https://github.com/princetongenizalab/pgp-text) + [Zenodo 10.5281/zenodo.15839056](https://zenodo.org/records/15839056). **CC BY-NC 4.0.** Machine-readable complement to Goitein's ~35,000-individual index. |
| **CBDB** — China, 7th–19th c. (pre-1500 = Tang–mid-Ming) | [cbdb.fas.harvard.edu](https://cbdb.fas.harvard.edu/) (Harvard / Academia Sinica / PKU) | Yes | (a)+(b) | **649,533** (May 2025); pre-1500 portion ~200,000–400,000 (note's range; **computable exactly from the dump**) | Full **SQLite + MS Access/SQL Server/MySQL** download (see below). **CC BY-NC-SA 4.0.** Largest pre-modern biographical DB in the world; filterable by dynasty. |
| **JBDB** — Japan, c.1550–1950 | [jbdb.jp](https://jbdb.jp/) | Yes | (a)/(d to edit) | Mostly post-1500; pre-1500 minimal | CBDB-modeled; no public bulk export/API. |
| **Who's Who in Korean History** — Korea | Academy of Korean Studies (한국역대인물종합정보시스템) | Yes | (a)/(c) | ~16,000 figures | Ancient–modern; Korean interface; no English bulk download. |
| **Siddham** — South Asia, ~early BCE–19th c. | [siddham.network](https://siddham.network/) (ERC-funded) | Yes | (a)+(b) | Person records present; no headline total | *Missed by the note.* Open-access; bulk data in [Zenodo communities](https://zenodo.org/communities/siddham/), FAIR. Sanskrit, Prakrit, Tamil, Telugu, Kannada, etc. South Asia is **not** the hard gap the note implies. |
| **DHARMA** — South/SE Asia epigraphy | [github.com/erc-dharma](https://github.com/erc-dharma) (ERC 809994) | Yes | (b) | Names embedded in inscription corpora; no aggregate count | *Missed by the note.* ~58 repos of TEI/XML, **CC-BY-4.0** (Pallava, Bengal charters, EIAD, Khmer, Nusantara…). |
| **MHD — Maya Hieroglyphic Database** | [mayadatabase.org](https://www.mayadatabase.org/) (CSU Chico, Looper) | Yes | (a)/(c) | Rulers/elites within texts; no distinct-person total | 207,539 grapheme entries; ~4,865 texts. Successor to the *New Catalog of Maya Hieroglyphs*. |
| **TWKM / classicmayan.org** — Classic Maya | [classicmayan.org/portal](https://classicmayan.org/portal/) (Bonn academies) | Yes | (a)+(b partial) | **302 individuals** (mostly rulers) + 91 events | *Missed by the note.* Aims to index ~10,000 script-carriers in XML/TEI; partial open-science exports (Zenodo). 15,000+ open images. |
| **Matrícula de Huexotzinco (1560)** — Mesoamerica | [loc.gov/item/2021668124](https://www.loc.gov/item/2021668124/) (Library of Congress) | Yes | (c) | >10,000 glyph-named individuals (confirms note) | Digitized manuscript image viewer, not queryable by person. Public domain. |
| **OCIANA** — Ancient North Arabian (Safaitic/Thamudic/Hismaic) | **OLD** `krc.orient.ox.ac.uk/ociana/` (Oxford) — **DEAD**; **NEW** [ociana.osu.edu](https://ociana.osu.edu/) (Ohio State) | **Moved → live at OSU** | (a)+(b) | ~40,000 inscriptions; distinct individuals not published (tens of thousands of "X son of Y") | Relaunched Sept 2024. **Full XML corpus** via Bodleian ORA ([uuid:08a60ae8…](https://ora.ox.ac.uk/objects/uuid:08a60ae8-e61d-486e-9ef1-836ca71d904c)). **Note's Oxford URL needs updating.** |
| **DASI** — pre-Islamic Arabia (Ancient South Arabian) | [dasi.cnr.it](https://dasi.cnr.it/) (CNR, Pisa) | Yes (bot-shielded) | (a)/(c) | ~8,400 ASA inscriptions; no name total | *Missed by the note.* South-Arabian counterpart to OCIANA. Anti-bot blocks automated fetches; figures from secondary sources. |
| **Hatra Aramaic inscriptions** — Mesopotamia | print: Marcato (2018) | n/a | (e) | 376 personal names | No online DB. |

## Databases worth pulling data from (bulk download / API)

Ranked roughly by value for re-deriving named-individual counts. Exact download targets:

1. **CBDB (highest value).** Full standalone DB, **CC BY-NC-SA 4.0**.
   - **SQLite (recommended):** `https://huggingface.co/datasets/cbdb/cbdb-sqlite/resolve/main/latest.zip` — current build `cbdb_20260314.sqlite3` (2026-03-14). Repo with scripts/metadata: [github.com/cbdb-project/cbdb_sqlite](https://github.com/cbdb-project/cbdb_sqlite).
   - **MS Access / SQL Server / MySQL:** [Harvard Dataverse doi:10.7910/DVN/PAGGQS](https://doi.org/10.7910/DVN/PAGGQS). Landing page: [Download CBDB Standalone Database](https://cbdb.hsites.harvard.edu/download-cbdb-standalone-database).
   - **Pre-1500 count:** query the persons table on index/death year `< 1500` (or by dynasty code). Converts the note's guessed "200,000–400,000" into an exact figure.
2. **Trismegistos People.** [Data Services](https://www.trismegistos.org/dataservices/) — PerResponder JSON + PerRDF API (`?id=<TM_Per_ID>`), **CC BY-SA 4.0**. Directly gives ~388,901 individuals (Egypt).
3. **LGPN.** OpenAPI/REST endpoint at `clas-lgpn5.classics.ox.ac.uk:8080/exist/apps/lgpn-api/`; TEI/XML deposit at ORA. ~400,000 Greek individuals. Attribution, non-commercial.
4. **EDH (Epigraphic Database Heidelberg).** CSV / JSON / SPARQL / EpiDoc, **CC BY-SA 4.0**, models persons explicitly. ETL: [github.com/sdam-au/EDH_ETL](https://github.com/sdam-au/EDH_ETL). Best lever on the very rough Roman distinct-individual estimate.
5. **CDLI.** Daily catalogue CSV + ATF transliterations at [github.com/cdli-gh/data](https://github.com/cdli-gh/data); CTS API. Artifacts not persons, but the substrate for cuneiform name-extraction.
6. **PNA / Oracc.** Full data in the Oracc JSON corpus [github.com/oracc/json](https://github.com/oracc/json) (`/projects.json` → `/pnao/manifest.json` → `corpusjson/`), **CC0**. >25,000 Neo-Assyrian individuals; plus the open 17,000-person social-network extract.
7. **Prosobab.** Full relational-DB dump at [Zenodo 6642356](https://zenodo.org/record/6642356), **CC BY-NC 4.0**. ~21,000 Neo-Babylonian persons.
8. **PIR.** JSON REST API + CSV via [github.com/telota/PIR](https://github.com/telota/PIR). ~14,000–15,000 Roman elite.
9. **OpenDomesday.** Public JSON API, no key: [opendomesday.org/api/](https://opendomesday.org/api/). Raw data at U. Hull.
10. **People of Medieval Scotland.** KDL CKAN dataset (RDF + API), Creative Commons: [data.kdl.kcl.ac.uk](https://data.kdl.kcl.ac.uk/dataset/people-of-medieval-scotland-project-1093-1371). ~21,000.
11. **PmbZ.** Open-access full-text DB at [telota.bbaw.de/pmbz](https://telota.bbaw.de/pmbz/). ~21,500 Byzantine.
12. **Princeton Geniza Project.** CSV exports [github.com/princetongenizalab/pgp-metadata](https://github.com/princetongenizalab/pgp-metadata) + [Zenodo 15839056](https://zenodo.org/records/15839056), **CC BY-NC 4.0**. 1,802 persons / ~35,855 documents.
13. **DHARMA.** ~58 TEI/XML inscription corpora on GitHub: [github.com/erc-dharma](https://github.com/erc-dharma), **CC-BY-4.0** (South/SE Asia).
14. **Siddham.** Bulk data in [Zenodo communities](https://zenodo.org/communities/siddham/) (South Asia).
15. **OCIANA.** Full XML corpus via Bodleian ORA ([uuid:08a60ae8…](https://ora.ox.ac.uk/objects/uuid:08a60ae8-e61d-486e-9ef1-836ca71d904c)).
16. **EDCS (via Lat-Epig).** Search-only on site, but [Lat-Epig](https://github.com/mqAncientHistory/Lat-Epig) scrapes results to TSV. ~542,000 inscriptions.
17. **TWKM / classicmayan.org.** Partial open-science exports (XML/TEI, Zenodo). 302 individuals.

*Reference, not a person source:* **Pleiades** ([pleiades.stoa.org](https://pleiades.stoa.org/)) — gazetteer of places (CC BY bulk dumps); a good model for how a person-aggregator could publish, but out of scope for counts.

## Corrections to the existing note

- **EDCS inscription count.** Note: "~509,600 Latin inscriptions … (as of 2018)". Now **~542,496** (Latin + Greek), hosted at U. Zurich, under renewal since 2024. Update figure and host.
- **CDLI artifact count.** Note: "~320,000+ … out of an estimated 500,000+". CDLI has now **crossed ~500,000 catalogued artifacts** (Dec 2025). The ~320,000 figure is stale. (Still an artifact catalogue, not a person count.)
- **BDTNS.** Now **105,187 tablets** (May 2026), slightly above the note's 104,923. Host cert is broken — cite the CESGA mirror [bdtns.cesga.es](https://bdtns.cesga.es/).
- **ODNB.** Note's "50,113 articles / 54,922 lives" is the **2004 print figure**; online edition is now **60,000+**. Pre-1500 share is **~5,000 "medieval lives"** (≈9–10%), per [Summerson (2018)](https://blog.oup.com/2018/10/medieval-dictionary-national-biography/) — firmer than the note's "a few thousand". ODNB is **paywalled**, unlike most others here.
- **PNA figure confirmed.** "more than 25,000 individuals … over 17,000" is correct — the two numbers are distinct (25,000 = full printed PNA; 17,000 = the open social-network extract).
- **Princeton Geniza.** Goitein's ~35,000-individual index stands, but the machine-readable PGP has only **1,802 person records** against ~35,855 *documents* — don't conflate documents with persons.
- **OCIANA URL is dead.** `http://krc.orient.ox.ac.uk/ociana/` no longer resolves; relaunched at **[ociana.osu.edu](https://ociana.osu.edu/)** (Sept 2024). Distinct-individual count still unpublished — the note's open question #5 remains open.
- **CBDB pre-1500 portion.** Upgrade, not correction: the "200,000–400,000" guess can be computed exactly from the SQLite dump. Total has grown to ~650,000 (May 2025), so the pre-1500 number may be slightly higher than when the range was set.
- **SNAP:DRGN is defunct.** The note's worry about double-counting across LGPN / TM / PIR can't be solved with SNAP — its aggregated triplestore (~650,000 records) has expired; it is now a standards/cookbook project only.

## Databases the note missed (now added above)

- **EDH** (Roman, person-modeled, fully open) — *high value*, the best route to a defensible Roman distinct-individual count.
- **Princeton Geniza Project** (machine-readable Geniza complement to Goitein).
- **Siddham** + **DHARMA** (South/SE Asia) — the note treats South Asia as a near-total gap; these are live, queryable, and bulk-downloadable, so the gap is narrower than stated.
- **TWKM / classicmayan.org** (Classic Maya, 302 individuals).
- **DASI** (Ancient South Arabian) — counterpart to OCIANA's North Arabian corpus.
- **Who's Who in Korean History** (~16,000 figures).
- **CIL "Datenbank ACE"** — the note cites CIL counts but not its live online DB.
- **Genuine remaining gaps:** Indian inscription corpora (*Epigraphia Indica*, *South Indian Inscriptions*) exist only as digitized text series, not indexed person-databases; no Vietnamese prosopography; no queryable Meroitic / Old Nubian / Ge'ez name DB.

---

*Provenance: merged from four independent verification passes on 2026-06-21 — a single-pass audit plus three regional deep-dives (ANE/Egypt/Greek; Roman/Byzantine/Medieval/Islamic; China/Asia/Americas/Arabia). Where figures or access modes conflicted, the regional pass (which checked each site directly) was preferred over the single-pass audit.*
