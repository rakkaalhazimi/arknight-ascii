import os
import pywhatkit as kt

IMG_DIR = "frame"
TEXT_DIR = "ascii"

for image_name in os.listdir(IMG_DIR):

    in_ = os.path.join(IMG_DIR, image_name)
    out = os.path.join(TEXT_DIR, os.path.splitext(image_name)[0])

    kt.image_to_ascii_art(in_, out)

    print(f"Write to {out}.txt", end="\r")