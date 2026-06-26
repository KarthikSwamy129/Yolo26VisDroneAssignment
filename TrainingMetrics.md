# Training Summary

## Model

YOLO26l

## Training Configuration

| Parameter | Value |
|-----------|------:|
| Epochs | 50 |
| Batch Size | 16 |
| Image Size | 1280 × 1280 |
| Optimizer | Auto |
| Learning Rate | 0.01 |
| Dataset | VisDrone2019 |
| GPU | NVIDIA RTX 4080 SUPER |

## Final Validation Results

The following results correspond to the **best checkpoint (`best.pt`)**, evaluated separately on the VisDrone validation dataset.

| Metric | Value |
|---------|------:|
| Precision | **0.670** |
| Recall | **0.593** |
| mAP50 | **0.604** |
| mAP50-95 | **0.384** |

## Model Information

- Parameters: 24.75M
- GFLOPs: 86.1
- Inference Speed: 4.3 ms/image

## Notes

The reported metrics were obtained by running a separate validation of the best saved model (`best.pt`) after training. These values correspond to the results reported in the accompanying project report.
