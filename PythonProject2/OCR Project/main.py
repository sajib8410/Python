from PIL import Image
import pytesseract

image_input= "image.jpg"
image_open= Image.open(image_input)
text= pytesseract.image_to_string(image_open)
print(text)