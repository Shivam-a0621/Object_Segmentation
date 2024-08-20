import torchvision.transforms as T
import torch

class preprocess:
    def __init__(self,image):
        self.image= image
    
    
    def preprocessed_image(self):
        preprocess = T.Compose([
        T.ConvertImageDtype(torch.float32),   
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  
                    ]) 
        
        return preprocess(self.image).unsqueeze(0) 
        
      