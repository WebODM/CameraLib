import json
import os
import glob
import logging
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


def read_xanylabeling_annotations(labels_dir: str) -> list[dict[str, Any]]:
    """Read an annotation file generated with X-AnyLabeling (https://github.com/CVHub520/X-AnyLabeling)
    
    Args:
        labels_dir (str): Path to a directory containing X-AnyLabeling labels.
    
    Returns:
        Annotations (list[dict[str, Any]]): A list of annotations with image, coordinates, properties, and normalized fields.
    """
    files = glob.glob(os.path.join(labels_dir, "*.json")) + glob.glob(os.path.join(labels_dir, "*.JSON"))
    annotations = []

    for fi in files:
        with open(fi, 'r') as f:
            j = json.load(f)
    
        annotations += [{
                'image': os.path.basename(j['imagePath']),
                'coordinates': s['points'],
                'properties': {
                    'label': s.get('label')
                },
                'normalized': False,
            }for s in j['shapes']]
    
    return annotations


def read_yolov7_annotations(labels_dir: str, image_suffix: str = '.JPG') -> list[dict[str, Any]]:
    """Read an annotation directory in YOLOv7 format
    
    Args:
        labels_dir (str): Path to a directory containing YOLOv7 labels.
        image_suffix (str): Extension of the target images.
    
    Returns:
        Annotations (list[dict[str, Any]]): A list of annotations with image, coordinates, properties, and normalized fields.
    """

    files = glob.glob(os.path.join(labels_dir, "*.txt")) + glob.glob(os.path.join(labels_dir, "*.TXT"))
    annotations = []

    for fi in files:
        with open(fi, 'r') as f:
            lines = [l for l in f.read().split("\n") if l.strip() != ""]  
            for line in lines:
                parts = line.split(" ")
                if len(parts) == 5:
                    try:
                        label, x_center, y_center, width, height = [float(p) for p in parts]
                        xmin = x_center - width / 2.0
                        ymin = y_center - height / 2.0
                        annotations.append({
                            'image': Path(fi).with_suffix(image_suffix).name,
                            'label': label,
                            'bbox': {
                                'xmin': xmin,
                                'xmax': xmin + width,
                                'ymin': ymin,
                                'ymax': ymin + height
                            }
                        })
                    except ValueError as e:
                        logger.warning(f"Cannot parse values in {line} ({fi})")
                else:
                    logger.warning(f"Cannot parse line {line} ({fi})")
        
    return [{
            'image': a['image'],
            'coordinates': [
                            [a['bbox']['xmin'], a['bbox']['ymin']],
                            [a['bbox']['xmax'], a['bbox']['ymin']],
                            [a['bbox']['xmax'], a['bbox']['ymax']],
                            [a['bbox']['xmin'], a['bbox']['ymax']]
                           ],
            'properties': {
                'label': a['label']
            },
            'normalized': True,
        }for a in annotations]