import os

from PIL import Image



def resize(im, n_width):
    width, height = im.size
    ratio = height/width
    n_height = int(ratio*n_width)
    resize_img = im.resize((n_width, n_height))
    return resize_img

files = os.listdir("IMAGE")
extension = ["jpg", "jpeg", "gif", "png", "cr3"]
for file in files:
    ext = file.split(".")[-1]
    if ext in extension:
        img = Image.open("IMAGE/"+file)
        im_resize = resize(img, 300)
        filepath = f"RESIZED/{file}"
        im_resize.save(filepath)

