import torch
from torchvision.io import read_image
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights
from torchvision.transforms.functional import to_pil_image
import matplotlib.pyplot as plt


class SegmentImage:
    def __init__(self):
        
        self.weights = FCN_ResNet50_Weights.DEFAULT
        self.model = fcn_resnet50(weights=self.weights)
        self.model.eval()
        
        
    def get_segments(self,input_img):
        with torch.no_grad():
            output = self.model(input_img)['out']
            segmented_output = torch.argmax(output.squeeze(), dim=0).byte()
            
        return output,segmented_output    
    
    
          
        
        
        
