from ultralytics import YOLO

model = YOLO('yolov8x')
results = model.predict('vidéos/vidéos1.mp4', save=True)
print(results[0])
for box in results[0].boxes:
    print(box)