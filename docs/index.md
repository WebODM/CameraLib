# CameraLib

CameraLib is a Python library for forward and backward projection of 2D image coordinates to geographic coordinates on ODX datasets.

Use it to answer questions such as:

- Given a pixel coordinate in an image, where does it correspond on the map?
- Given a location on the map, which images and pixels correspond to it?

![CameraLib overview](https://github.com/user-attachments/assets/00d14b1f-16fe-4123-a171-6ef3b774aeb9)

## Quickstart

Make sure your ODX project has an elevation model available (by processing with `--dsm`), then:

```python
from cameralib import Projector

p = Projector("/dataset/brighton")
hits = p.world2cams(46.8423725961765, -91.99395518749954)
world_points = p.cam2world("DJI_0028.JPG", [(3576.52, 898.97)])
```

## Learn More

- See the [Installation](installation.md) guide.
- Explore [Examples](examples.md).
- Browse the [API Reference](reference.md).