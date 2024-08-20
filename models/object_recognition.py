from ultralytics import YOLO

class ObjectDetect:
    def __init__(self,image):
        self.image= image
        self.model= YOLO("yolov8n.pt")

    def detect(self):
        results= self.model.predict(self.image,save=True,)  
        return results