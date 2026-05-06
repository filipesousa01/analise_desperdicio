from ultralytics import YOLO

from roboflow import Roboflow
rf = Roboflow(api_key="COLOQUE_SUA_CHAVE_AQUI")
project = rf.workspace("NOME_DO_SEU_WORKSPACE").project("NOME_DO_SEU_PROJETO")
version = project.version(26)
dataset = version.download("yolov8")
                
                                       
def main():
    model = YOLO("yolov8n.pt")

    model.train(
    data="data.yaml",
    epochs=150,
    imgsz=640,
    batch=8,                     # ou -1
    device=0,
    workers=4,
    amp=True,
    lr0=0.0005,                  # mais baixo
    weight_decay=0.001,          # mais regularização
    warmup_epochs=5,
    patience=30,
    # Augmentações

    degrees=45,
    translate=0.1,
    scale=0.1,
    fliplr=0.5,
    mosaic=1.0,
    mixup=0.5,
    close_mosaic=15
)

if __name__ == "__main__":
    main()