from PIL import Image
import os

for i in os.listdir():
    if i.endswith(".jpg"):
        path = os.path.join(os.getcwd())+i
        with open(path, 'w') as file:
            img = Image.open(path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(path)

