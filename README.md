# Attempts at Python 3.x + GIS work with pyshp, osgeo, matplotlib.basemap

Learning about Python and GIS as I go...

Attempting to do everything in Python 3.x, [as supplied by Anaconda](https://docs.continuum.io/anaconda/pkg-docs).

## Current status 


### Plotting on maps

Trying to use [matplotlib's basemap](https://github.com/matplotlib/basemap) to do geospatial visualizations.

- [x] Installed basemap via `conda install basemap`
- [x] Created earthquake scatterplot on Earth map layer: [gist](https://gist.github.com/dannguyen/eb1c4e70565d8cb82d63)

    <img src="assets/images/basemap-quakes.png" alt="basemap earthquakes">
- [x] Rendered mapviz as part of matplotlib grids [viz_subplotmaps.py](viz_subplotmaps.py)
    
    <img src="assets/images/worldwide-m6-quakes-2000-2015-subplots.png" alt="basemap earthquakes">

- [ ] Use basemap to read shapefile and project
  - [x] Successfully plotted Census shapefile that's already in epsg:4326
    
    <a id="mark-plot-census-checkoff"></a>
    Check it out: [plot_census_counties.py](plot_census_counties.py)

    <img src="assets/images/census-counties-20m.png" alt="census-counties-aea">  

  - [ ] Unable to open shapefiles that aren't in lat/lng format   
    


### Using pyshp

Trying to re-project a shapefile in Python using [pyshp](https://pypi.python.org/pypi/pyshp):

- [x] Installed pyshp `pip install pyshp`
- [x] Attempted to emulate example: [Reproject a Polygon Shapefile using PyShp and PyProj](https://glenbambrick.com/2016/01/24/reproject-shapefile/)
- [ ] Attempted to convert bayarea_zipcodes file to esri:4326: [bayarea_foo.py](bayarea_foo.py), but failed: [bayarea_mapfoo.py](bayarea_mapfoo.py)


### Using pyproj

Projecting coordinates with [pyproj](https://github.com/jswhit/pyproj)

- [x] Installed pyproj via `conda install pyproj`
- [x] Successfully projected coordinates
  - See use of pyproj to translate X/Y coordinates in NYPD stops-and-frisks data to lng/lat: [dannguyen/python-notebooks-data-wrangling -- wrangling-nypd-frisks.py](https://github.com/dannguyen/python-notebooks-data-wrangling/blob/master/scripts/wrangling-nypd-frisks.py)
  - See early attempts at using pyproj (and caveat about its configuration): [Getting inaccurate results converting from New York State projection to NAD83 with Python's pyproj](http://gis.stackexchange.com/questions/181667/getting-inaccurate-results-converting-from-new-york-state-projection-to-nad83-wi)   
