from ultralytics import YOLO
from collections import Counter

class Detector():
    def __init__(self):
        self.model = YOLO("./training/runs/detect/train/weights/best.pt")
    
    # makes object prediction.
    def predict(self, frame):
        result = self.model.track(frame, persist=True)[0]

        # Get the boxes and track IDs
        if result.boxes:

            # Visualize the result on the frame
            frame = result.plot()

            class_ids = result.boxes.cls.cpu().numpy().astype(int)
            class_names = [result.names[int(cls)] for cls in class_ids]
            class_counts = Counter(class_names)
            classes = f"Detected classes: {dict(class_counts)}"
            classes = classes.replace("{", "")
            classes = classes.replace("}", "")
        else:
            classes = f"No object(s) detected."
        return frame, classes