##REQUIREMENTS 
#gradio
#scikit-image
#pillow 
#------------------
#-----------------------------------------------
#CODE 
import gradio as gr
from skimage.filters import threshold_otsu
from PIL import Image
import numpy as np
def segmentor(image):
    img_np=np.array(image.convert("L"))
    threshold=threshold_otsu(img_np)
    binary=img_np>threshold
    return Image.fromarray(binary)

image_input=gr.Image(type="pil",label="Upload your image")
image_output=gr.Image(label="Image processed")
iface=gr.Interface(fn=segmentor,inputs=image_input,
                   outputs=image_output,title="FindSkinLesion",
                   description="An app to make a segmentation on image in input to predict if there is a skin lesion or not")

iface.launch(share=True)