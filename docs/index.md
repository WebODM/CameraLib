# CameraLib

CameraLib is a Python library for forward and backward projection of 2D image coordinates to geographic coordinates on [ODX](https://github.com/WebODM/ODX) datasets.

Use it to answer questions such as:

- Given a pixel coordinate in an image, where does it correspond on the map?
- Given a location on the map, which images and pixels correspond to it?

![CameraLib overview](https://github.com/user-attachments/assets/00d14b1f-16fe-4123-a171-6ef3b774aeb9)

## Quickstart

Make sure your ODX project has an elevation model available (by processing with `--dsm`), then:

```python
from cameralib import Projector
p = Projector("/dataset/brighton")
p.world2cams(46.8423725961765, -91.99395518749954)
# --> [{'filename': 'DJI_0028.JPG', 'x': 3576.5223779005346, 'y': 898.9714056819935}, {'filename': 'DJI_0027.JPG', 'x': 3640.8434954842614, 'y': 1670.683552000412}, {'filename': 'DJI_0031.JPG', 'x': 2066.0067963232805, 'y': 1252.4355627370903}, {'filename': 'DJI_0030.JPG', 'x': 2065.2268758465634, 'y': 255.93742225443987}, {'filename': 'DJI_0032.JPG', 'x': 1979.1241736591578, 'y': 2153.9211152055022}]
p.cam2world("DJI_0028.JPG", [(3576.52, 898.97)])
# --> [(46.84237264716458, -91.9939552609622, 165.27200317382812)]
```

## Learn More

- See the [Installation](installation.md) guide.
- Explore [Examples](examples.md).
- Browse the [API Reference](reference.md).