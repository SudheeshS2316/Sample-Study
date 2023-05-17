import pytesseract
from PIL import Image

# Load the image
image = Image.open('hindi.png')

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
