import sys
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


print("OpenCV version" + cv2.__version__)


def variance_of_laplacian(image):
    """
    compute the Laplacian of the image and return the focus measure
    """
    return cv2.Laplacian(image, cv2.CV_64F).var()


def process_video(path, threshold, step, save_path):
    vidcap = cv2.VideoCapture(path)

    success, image = vidcap.read()
    count = 0
    blurryFrame = 0
    savedFrame = 0
    frameStep = 0

    print("Working...")

    while success:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)

        if frameStep == step:
            if fm > threshold:
                savedFrame += 1
                image_path = os.path.join(save_path, "frame%d.png" % count)
                cv2.imwrite(image_path, image)
            frameStep = 0

        if fm < threshold:
            blurryFrame += 1

        success, image = vidcap.read()
        count += 1
        frameStep += 1

    print("Done!")


def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select video file",
                                           filetypes=(("Video files", "*.mp4;*.avi;*.mkv;*.flv;*.mov"),
                                                      ("All files", "*.*")))
    return file_path


def ask_parameters():
    threshold = simpledialog.askfloat("Threshold", "Enter the threshold value:",
                                      initialvalue=100.0, minvalue=0)
    step = simpledialog.askinteger("Step", "Enter the frame step size:",
                                    initialvalue=1, minvalue=1)
    save_path = filedialog.askdirectory(title="Select directory to save frames")
    return threshold, step, save_path


def main():
    root = tk.Tk()
    root.withdraw()

    print("Select video file")
    video_path = open_file_dialog()

    if not video_path:
        sys.exit("No video file selected")

    print("Enter parameters")
    threshold, step, save_path = ask_parameters()

    process_video(video_path, threshold, step, save_path)


if __name__ == "__main__":
    main()
