import requests
from shutil import unpack_archive
from pathlib import Path
URL = 'http://apps.sfgov.org/datafiles/view.php?file=sfgis/bayarea_zipcodes.zip'
DDIR = Path('data', Path(URL).stem)
DDIR.mkdir(parents=True, exist_ok=True)
ZIP_PATH = DDIR.joinpath(Path(URL).name)

resp = requests.get(URL)
with ZIP_PATH.open('wb') as zf:
    zf.write(resp.content)
# unpack it
unpack_archive(str(ZIP_PATH), extract_dir=str(DDIR))
