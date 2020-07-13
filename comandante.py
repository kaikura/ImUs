import os
import sys
import time
sys.path.append('/Users/Manuk/Downloads/capturing-images-from-webcam-using-opencv-python-masterreloaded')
os.system("python3 /Users/Manuk/Downloads/capturing-images-from-webcam-using-opencv-python-masterreloaded/webcam-capture-v1.01.py")
os.system(
    'python3 /Users/Manuk/Downloads/face_morpher-dlib/facemorpher/purpose.py '
    '--principale=/Users/Manuk/Downloads/photos_morph '
    '--secondario=/Users/Manuk/Downloads/images_morph2_intermediate '
    '--A=/Users/Manuk/Downloads/images_morph2/A '
    '--B=/Users/Manuk/Downloads/images_morph2/B '
    '--C=/Users/Manuk/Downloads/images_morph2/C '
    '--destinazione=/Users/Manuk/Downloads/morphdef.avi')
time.sleep(5)
os.system('/Users/Manuk/Documents/Processing/videoOSC/application.macosx/source/videoOSC/application.macosx64/videoOSC.app/Contents/MacOS/videoOSC')