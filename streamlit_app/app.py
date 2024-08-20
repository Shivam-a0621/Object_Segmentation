import streamlit as st
from utils.preprocessing import preprocess
from models.segmentation_model import SegmentImage
from utils.visualization import visualization
from PIL import Image
import os
from torchvision.io import read_image
from torchvision.transforms.functional import to_pil_image





UPLOAD_FOLDER = 'images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    

def save_image(uploaded_file):
    # Save the uploaded image
    image = Image.open(uploaded_file)
    image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    image.save(image_path)
    return image_path


def preprocess_image(image_path):
    
    input_image = read_image(image_path)
    pp= preprocess(input_image)
    output_image = pp.preprocessed_image()
    
    return output_image


def get_segmentation_masks(image):
    SI= SegmentImage()
    out_put, seg_ment= SI.get_segments(image)
    return seg_ment
    
def home_page():
    st.title("Home Page")
    st.write("Welcome to the app. Use the buttons below to interact with different functions.")
    
   

def main():
    
    
    st.sidebar.title("Navigation")
    
    page = st.sidebar.radio("Go to..",["Home","Upload Images","Segment image","Detect Object",])

    
    
def main():
    # Initialize the session state
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    if st.session_state.page == "Home":
        home_page()
    

if __name__ == "__main__":
    main()    

