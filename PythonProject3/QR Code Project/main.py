import qrcode
img= qrcode.make("https://chatgpt.com/")
type(img)
img.save("demo.png")