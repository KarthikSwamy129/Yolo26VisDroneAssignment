# An Efficient Aerial Small Object Detection Pipeline Using YOLO26l and EigenCAM

This repository contains the implementation and experimental results for the project **"An Efficient Aerial Small Object Detection Pipeline Using YOLO26l and EigenCAM."** The project focuses on improving small object detection in aerial imagery using the YOLO26l object detection framework trained on the VisDrone2019 dataset.

## Authors

- Urooj Murad
- Karthik M. Swamy
- Chun Lo

---

## Project Overview

Small object detection in aerial imagery is challenging because targets often occupy only a few pixels and appear in dense, cluttered scenes. This project proposes an efficient detection pipeline based on **YOLO26l**, combined with **EigenCAM** visualization for model interpretability and **TensorRT** optimization for real-time deployment.

The proposed framework was trained and evaluated on the **VisDrone2019 Detection Dataset** and demonstrates competitive detection accuracy while maintaining low inference latency.

---

## Features

- YOLO26l-based object detector
- Fine-tuned on the VisDrone2019 dataset
- High-resolution training
- EigenCAM attention visualization
- Threshold-based clustering analysis
- TensorRT deployment optimization
- Real-time inference capability

---

## Dataset

This project uses the **VisDrone2019 Detection Dataset**.

The dataset can be downloaded from the official VisDrone website:

https://github.com/VisDrone/VisDrone-Dataset

After downloading the dataset, update the dataset path in the training configuration before running the training scripts.

---

## Training Configuration

| Parameter | Value |
|-----------|------:|
| Model | YOLO26l |
| Epochs | 50 |
| Image Size | 1280 × 1280 |
| Batch Size | 16 |
| Optimizer | Auto |
| Device | NVIDIA RTX 4080 SUPER |
| Dataset | VisDrone2019 |

---

## Final Validation Results

The following results correspond to the **best checkpoint (`best.pt`)**, which was evaluated separately on the VisDrone validation dataset.

| Metric | Value |
|---------|------:|
| Precision | **0.670** |
| Recall | **0.593** |
| mAP50 | **0.604** |
| mAP50-95 | **0.384** |
| Inference Speed | **4.3 ms/image** |

---



## Hardware

- GPU: NVIDIA RTX 4080 SUPER
- CUDA
- PyTorch
- Ultralytics YOLO26

---



## License

This repository is intended for academic and educational purposes.
