# VisDrone2019 Dataset

This project was trained and evaluated using the **VisDrone2019 Detection Dataset**, a benchmark designed for object detection in aerial imagery captured by unmanned aerial vehicles (UAVs).

## Dataset Information

- Dataset: VisDrone2019 Detection
- Number of Classes: 10
- Image Resolution: Various
- Task: Object Detection

### Object Categories

- Pedestrian
- People
- Bicycle
- Car
- Van
- Truck
- Tricycle
- Awning-tricycle
- Bus
- Motor

## Download

The dataset can be downloaded from the official VisDrone repository:

https://github.com/VisDrone/VisDrone-Dataset

or

http://aiskyeye.com/

After downloading, organize the dataset according to the Ultralytics YOLO format before training.

## Dataset Structure

```
VisDrone/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── data.yaml
```

The dataset itself is not included in this repository because of its large size.
