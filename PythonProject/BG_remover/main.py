from PIL import Image
from rembg import remove

input_img= "input_image.png"

input_img_open= Image.open(input_img)

output_img= remove(input_img_open)

output_img.save("output_image.png")

print("Precess Completed.....")