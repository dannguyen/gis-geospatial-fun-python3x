from shutil import unpack_archive
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

SHP_BASENAME = 'bayarea_zipcodes'
DDIR = Path('data', SHP_BASENAME)
NEWPREFIX = 'epsg_4326--'
SHP_NAME = DDIR.joinpath(NEWPREFIX + SHP_BASENAME)

fig, ax = plt.subplots()
m = Basemap(ax=ax)
m.readshapefile(str(SHP_NAME), 'stuffwhatisthis')


## Current error

# <ipython-input-10-e13d46807975> in <module>()
# ----> 1 m.readshapefile(str(SHP_NAME), 'stuffwhatisthis')

# /Users/dtown/.pyenv/versions/anaconda3-2.5.0/lib/python3.5/site-packages/mpl_toolkits/basemap/__init__.py in readshapefile(self, shapefile, name, drawbounds, zorder, linewidth, color, antialiased, ax, default_encoding)
#    2144         info = (shf.numRecords,shptype,bbox[0:2]+[0.,0.],bbox[2:]+[0.,0.])
#    2145         npoly = 0
# -> 2146         for shprec in shf.shapeRecords():
#    2147             shp = shprec.shape; rec = shprec.record
#    2148             npoly = npoly + 1

# /Users/dtown/.pyenv/versions/anaconda3-2.5.0/lib/python3.5/site-packages/mpl_toolkits/basemap/shapefile.py in shapeRecords(self)
#     541         shapeRecords = []
#     542         return [_ShapeRecord(shape=rec[0], record=rec[1]) \
# --> 543                                 for rec in zip(self.shapes(), self.records())]
#     544
#     545 class Writer:

# /Users/dtown/.pyenv/versions/anaconda3-2.5.0/lib/python3.5/site-packages/mpl_toolkits/basemap/shapefile.py in records(self)
#     508         """Returns all records in a dbf file."""
#     509         if not self.numRecords:
# --> 510             self.__dbfHeader()
#     511         records = []
#     512         f = self.__getFileObj(self.dbf)

# /Users/dtown/.pyenv/versions/anaconda3-2.5.0/lib/python3.5/site-packages/mpl_toolkits/basemap/shapefile.py in __dbfHeader(self)
#     444             self.fields.append(fieldDesc)
#     445         terminator = dbf.read(1)
# --> 446         assert terminator == b("\r")
#     447         self.fields.insert(0, ('DeletionFlag', 'C', 1, 0))
#     448

# AssertionError:

