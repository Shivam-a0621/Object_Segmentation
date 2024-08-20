import easyocr
import cv2


class Textextractor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.reader = easyocr.Reader(['en'], gpu=False)
        
    def extract(self):
        results = self.reader.readtext(self.image)
        txt = []
        for (_, t, _) in results:
            txt.append(t)
        return txt