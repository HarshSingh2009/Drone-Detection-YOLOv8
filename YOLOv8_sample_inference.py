from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.pt")  # load a pretrained model (recommended for training)

results = model("https://ultralytics.com/images/bus.jpg", show=True, save=True)  # predict on an image