import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Sending request
url= "https://interactivecares.com/"
response= requests.get(url, verify=False)

# HTML conversion
html = BeautifulSoup(response.text, "html.parser")

# Folder name
folder= "images"

# Finding all Image tags
allImages= html.find_all("img")

for i, img in enumerate(allImages):
    img_url= img.get('src')
    if not img_url:
        continue

    # Rebuilding Image path
    img_url= urljoin(url,img_url)

    # Image File name
    fileName= os.path.join(folder,f"image{i+1}.jpg")

    # Download
    try:
        imageResponse= requests.get(img_url)
        imageBinaryData= imageResponse.content
        with open(fileName,"wb") as file:
            file.write(imageBinaryData)
            print(f"Download Successful {fileName}")

    except Exception as e:
        print(f"Download Failed {img_url}")
