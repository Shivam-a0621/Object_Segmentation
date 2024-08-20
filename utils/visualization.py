import matplotlib.pyplot as plt
from torchvision.transforms.functional import to_pil_image


class visualization:
    def __init__(self,original_img,segmented_img):
        self.original_image = original_img
        self.segmented_image = to_pil_image(segmented_img.byte())
        
        
    def display_img(self):
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(to_pil_image(self.original_image.squeeze()))
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(self.segmented_image, cmap='jet')
        plt.title('Segmented Output')

        plt.show()