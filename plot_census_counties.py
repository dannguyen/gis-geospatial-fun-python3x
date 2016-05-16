"""
Plot U.S. Census Shapefiles using Albers Equal Area

https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
http://matplotlib.org/basemap/users/aea.html
http://gis.stackexchange.com/questions/141580/which-projection-is-best-for-mapping-the-contiguous-united-states/142093
"""


from pathlib import Path
from shutil import unpack_archive
import requests
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
IMG_PATH = Path('assets', 'images', 'census-counties-20m.png')

SHPFILE_URL = 'http://www2.census.gov/geo/tiger/GENZ2015/shp/cb_2015_us_county_20m.zip'
SHPFILE_ZIPPATH = Path('data', Path(SHPFILE_URL).name)
SHPFILE_NAME = Path('data', SHPFILE_ZIPPATH.stem, SHPFILE_ZIPPATH.stem)
SHPFILE_PATH = Path('data', SHPFILE_ZIPPATH.stem, SHPFILE_ZIPPATH.stem + '.shp')

SHPFILE_DIR = SHPFILE_PATH.parent
if not SHPFILE_PATH.exists():
    print("Can't find", SHPFILE_PATH)
    print("Downloading", SHPFILE_URL)
    SHPFILE_DIR.mkdir(parents=True, exist_ok=True)
    resp = requests.get(SHPFILE_URL)
    with SHPFILE_ZIPPATH.open('wb') as w:
        w.write(resp.content)

    unpack_archive(str(SHPFILE_ZIPPATH), extract_dir=str(SHPFILE_DIR))


fig, ax =  plt.subplots()
map = Basemap(ax=ax, projection='aea',
              llcrnrlon=-120, urcrnrlon=-62,
              llcrnrlat=21.5, urcrnrlat=50,
              lat_1=29.5, lat_2=45.5, lon_0=-96, lat_0=37.5)
map.drawmapboundary(fill_color='#34ACAF')
map.fillcontinents(color='#AA0078',lake_color='#34ACAF')
map.readshapefile(str(SHPFILE_NAME), 'stuff', linewidth=0.4, color="magenta")
ax.set_title("U.S. Census County Shapefile w/ Albers Equal Area Projection")
fig.savefig(str(IMG_PATH))
