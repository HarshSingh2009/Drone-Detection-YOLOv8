from ultralytics import YOLO


# model path
model_path = './YOLOv8 models/best.pt'

# Load model
model = YOLO(model_path) # load a custom fine-tuned model

class_names = {0: 'drone'}

drone_video_input_path = 'drone.mp4'
results = model(source=drone_video_input_path, save=True, conf=0.4, show=True)


