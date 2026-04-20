# Installation

## Package Install

```bash
pip install -U https://github.com/WebODM/CameraLib/archive/main.zip
```

CameraLib is developed and tested with Python 3.12.

## Required ODX Project Files

CameraLib requires these files from an ODX project:

- `odm_dem/dsm.tif` or `odm_dem/dtm.tif`
- `odm_report/shots.geojson`
- `cameras.json`

The directory names above are expected by the library and should not be renamed.