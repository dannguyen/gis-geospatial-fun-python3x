"""
A reproduction of code found at:
https://glenbambrick.com/2016/01/24/reproject-shapefile/
"""
from pathlib import Path
from pyproj import Proj, transform
import shapefile
SHP_BASENAME = 'bayarea_zipcodes'
DDIR = Path('data', SHP_BASENAME)
SHP_NAME = DDIR.joinpath(SHP_BASENAME)
NEWPREFIX = 'epsg_4326--'

# set the input projection of the original file.
INPUT_PROJ = Proj(init="esri:102643")
# set the projection for the output file.
OUTPUT_PROJ = Proj(init="epsg:4326")
# OUTPUT PRJ WKT
OUTPUT_WKTPRJ = Path('data', 'projections', 'epsg_4326.txt').read_text()



r_sf = shapefile.Reader(str(SHP_NAME))
w_sf = shapefile.Writer(r_sf.shapeType)


for shape in r_sf.shapes():
    # each shape has a list of geometry to add to new file
    listpoly = []
    if len(shape.parts) == 1:
        for x, y in shape.points:
            newxy = transform(INPUT_PROJ, OUTPUT_PROJ, x, y)
            listpoly.append(list(newxy))
        ### add geometry to new file
        w_sf.poly(parts=[listpoly]) ## REFACTORTK
    else: # more than one part to the geometry
        shparts = shape.parts
        shpoints = shape.points
        shparts.append(len(shpoints)) # ...?
        for i in range(len(shparts) - 1):
            listparts = []
            coordct = shparts[i]
            endcoord = coordct + abs(coordct - shparts[i + 1])
            for j in range(coordct, endcoord):
                for coords in shpoints[j:endcoord]:
                    x, y = coords
                    newxy = transform(INPUT_PROJ, OUTPUT_PROJ, x, y)
                    listparts.append(list(newxy))
            listpoly.append(listparts)

        ### add geometry to new file
        w_sf.poly(parts=listpoly) ## REFACTORTK


# save to shapefile
out_baseshp = NEWPREFIX + SHP_BASENAME
out_shpname = DDIR.joinpath(out_baseshp + '.shp')
w_sf.save(str(out_shpname))

# generate PRJ file
out_prjname = DDIR.joinpath(out_baseshp + '.prj')
with out_prjname.open('w') as wf:
    # via http://spatialreference.org/ref/epsg/4326/prettywkt/
    wf.write(OUTPUT_WKTPRJ)
