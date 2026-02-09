from transformers import pipeline
from PIL import Image

# Load pre-trained image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Load image (replace with your image file path)
image = Image.open("image.jpg")

# Generate caption
caption = captioner(image)

print(caption[0]['generated_text'])
