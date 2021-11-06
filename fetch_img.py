import os
import cv2

VID = "Arknights Animation Music Video – Untitled World.mkv"
IMG_DIR = "frame"

if not os.path.exists(IMG_DIR):
    os.mkdir(IMG_DIR)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    length = int(vidcap.get(cv2. CAP_PROP_FRAME_COUNT))
    print(length)
    success = False

    fps = 24
    
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, count * 1000 / fps)    # added this line 
        success, image = vidcap.read()

        if image is None:
            break

        print(f"Read a new frame: {success} - {count}", end="\r")
        
        im_name = f"frame{count:04}.jpg"
        im_path = os.path.join(pathOut, im_name)
        cv2.imwrite(im_path, image)     # save frame as JPEG file

        count = count + 1

    

if __name__ == "__main__":
    extractImages(VID, IMG_DIR)