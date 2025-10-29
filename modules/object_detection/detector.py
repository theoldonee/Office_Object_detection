from ultralytics import YOLO

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
        
        return frame