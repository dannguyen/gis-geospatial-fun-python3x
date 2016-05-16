# http://basemaptutorial.readthedocs.io/en/latest/shapefile.html

from mpl_toolkits.basemap import Basemap
from pathlib import Path
import matplotlib.pyplot as plt
SHPFILE_PATH = Path('data', 'cb_2015_06_tract_500k', 'cb_2015_06_tract_500k' )

map = Basemap(llcrnrlon=-124.48, urcrnrlon=-114.13,
              llcrnrlat=32.53, urcrnrlat=42.01,
              resolution='i', projection='tmerc',
              lat_0 = 32, lon_0 = -120)
map.drawmapboundary(color='#333333', fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.readshapefile(str(SHPFILE_PATH), 'stuff')
plt.show()
