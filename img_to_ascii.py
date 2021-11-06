import os
import sys
from PIL import Image

IMG_DIR = "frame"
TEXT_DIR = "ascii"

if not os.path.exists(TEXT_DIR):
    os.mkdir(TEXT_DIR)

for image_name in os.listdir(IMG_DIR):

    img = Image.open(os.path.join(IMG_DIR, image_name))

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 160
    new_height = aspect_ratio * new_width * 0.45
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["*","S","#","&","@","$","%","*","!",":","."]
    
    
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    # write to a text file.
    textfn = os.path.splitext(image_name)[0] + ".txt"
    textpath = os.path.join(TEXT_DIR, textfn)
    with open(textpath, "w") as f:
        f.write(ascii_image)

    print(f"Write to {textpath}", end="\r")