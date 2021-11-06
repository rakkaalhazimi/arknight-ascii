import glob
import os
import time

TEXT_DIR = "ascii"
frame_ascii = []


def play_text(dir):
    

    for textfile in glob.glob(dir + "/*.txt"):
        with open(textfile, "r") as frame:
        
            frame_ascii.append(frame.read())
    else:
        input("Load complete: press enter to continue.")

    for index in range(0, len(frame_ascii), 2):
        print(frame_ascii[index])
        time.sleep(0.0404)
        os.system("cls")


if __name__ == "__main__":
    play_text(TEXT_DIR)