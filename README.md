This Python script uses OpenCV and tkinter to process a video file and extract frames based on a focus measure, which determines whether the frame is blurry or not. The extracted frames are saved to a specified directory.

Features
Select video files using a file dialog
Set custom focus measure threshold and frame step size
Save extracted frames to a specified directory
Requirements
Python 3.x
OpenCV (opencv-python)
tkinter (included in standard Python distribution)
To install OpenCV, run:
pip install opencv-python
Usage
Run the script: python main.py
Select a video file using the file dialog that appears.

Enter the focus measure threshold, frame step size, and the directory to save the extracted frames using the input dialogs.

The script will process the video and save the frames with a focus measure greater than the threshold in the specified directory.

License
This project is licensed under the MIT License - see the LICENSE file for details.
