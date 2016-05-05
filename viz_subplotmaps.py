from pathlib import Path
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILENAME = Path('data', 'usgs', 'worldwide-m6-quakes.csv')
OUTPUT_IMGNAME = Path('assets', 'images', 'worldwide-m6-quakes-2000-2015-subplots.png')
quakes = pd.read_csv(str(DATA_FILENAME), parse_dates=['time'])
# probably a better way to get year values
years = quakes['time'].dt.year.sort_values().unique()

ncol = 3 # hardcoded
nrow = int(len(years) / ncol)

fig, axlist = plt.subplots(ncol, nrow, figsize=(20, 10),
                           sharex=True, sharey=True)

for i in range(ncol):
    for j in range(nrow):
        n = (i * ncol) + j
        yr = years[n]
        qdf = quakes[quakes['time'].dt.year == yr]
        ax = axlist[i][j]
        earthmap = Basemap(ax=ax)
        earthmap.drawcoastlines(color='#555566', linewidth=1)
        # plot it
        ax.scatter(qdf['longitude'], qdf['latitude'])
        ax.set_title(str(yr))


fig.savefig(str(OUTPUT_IMGNAME))
