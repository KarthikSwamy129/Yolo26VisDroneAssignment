from ultralytics import YOLO

def main():
    # Load pretrained YOLO26l model
    model = YOLO("yolo26l.pt")

    # Train the model
    model.train(
        data="data.yaml",          # Update with your dataset path
        epochs=50,
        imgsz=1280,
        batch=16,
        device=0,                  # Change to your GPU index if needed
        workers=8,
        optimizer="auto",

        lr0=0.01,
        lrf=0.01,
        momentum=0.937,
        weight_decay=0.0005,

        warmup_epochs=3.0,
        warmup_momentum=0.8,
        warmup_bias_lr=0.1,

        box=7.5,
        cls=0.5,
        dfl=1.5,

        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,

        translate=0.1,
        scale=0.5,
        fliplr=0.5,
        flipud=0.0,

        mosaic=1.0,
        mixup=0.0,
        cutmix=0.0,
        copy_paste=0.0,

        close_mosaic=10,

        patience=100,
        pretrained=True,
        deterministic=True,
        seed=0,

        amp=True,
        plots=True,
        val=True,
        save=True
    )

if __name__ == "__main__":
    main()
