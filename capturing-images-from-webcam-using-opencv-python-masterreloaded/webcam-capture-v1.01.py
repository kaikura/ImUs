
import sys
import cv2
import numpy
import shutil
import os

os.chdir('/Users/Manuk/Downloads/capturing-images-from-webcam-using-opencv-python-masterreloaded')
sys.path.append('/Users/Manuk/Downloads/capturing-images-from-webcam-using-opencv-python-masterreloaded')

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
pictures_left=3
flag_thank_you=0
ipsum=10
fine=False

while True:
    try:


        if flag_thank_you == 0:
            check, frame = webcam.read()
            font = cv2.FONT_HERSHEY_TRIPLEX

            if frame is not None:
                bottomLeftCornerOfText = (int(numpy.size(frame, 1)/30), int(numpy.size(frame, 0) - numpy.size(frame, 0)/25))
                fontScale = 1
                fontColor = (2500, 200, 200)
                lineType = 2
                cv2.putText(frame, 'Hi dude! Put your face at the center of the ellipse and press space',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            lineType)
                #cv2.rectangle(frame, (int(numpy.size(frame, 1)/3), int(numpy.size(frame, 0)/16)), (int(numpy.size(frame, 1)/1.4), int(numpy.size(frame, 0)/1.15)), (255, 200, 200), 10 )

                cv2.ellipse(frame, (int(numpy.size(frame, 1)/2), int(numpy.size(frame, 0)/2)), (int(numpy.size(frame, 1)/4.3), int(numpy.size(frame, 0)/3.5)), 90, 0, 360, (255, 200, 200), 10)




            # print(check) #prints true as long as the webcam is running
       # print(frame) #prints matrix values of each framecd
        # Write some Text
        if fine == True:
            break

        bottomLeftCornerOfText = (int(numpy.size(frame, 1)/4.5), int(numpy.size(frame, 0) - numpy.size(frame, 0)/25))

        if flag_thank_you == 0:
            ipsum = 50;

            # cv2.putText(frame, 'Press space to do a selfie',
            #             bottomLeftCornerOfText,
            #             font,
            #             fontScale,
            #             fontColor,
            #             lineType)
            cv2.namedWindow("Capturing", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Capturing", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("Capturing", frame)

        else:
            check, frame = webcam.read()

            cv2.putText(frame, 'Thank you dear! Enjoy yor experience!;-)',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            cv2.imshow("Capturing", frame)
            cv2.rectangle(frame, (50, 50) , (100, 100), (255,0,0), 25)
            ipsum=ipsum-2;
            # time.sleep(3)



            # cv2.waitKey(1650)
            # cv2.destroyAllWindows()
            #
            # webcam = cv2.VideoCapture("trumphill.avi")
            # # Read until video is completed
            # while (webcam.isOpened()):
            #     # Capture frame-by-frame
            #     ret, frame = webcam.read()
            #     if ret == True:
            #
            #         # Display the resulting frame
            #         cv2.putText(frame, 'Thank you dear! Enjoy yor experience!:-)',
            #                     bottomLeftCornerOfText,
            #                     font,
            #                     fontScale,
            #                     fontColor,
            #                     lineType)
            #
            #
            #         cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
            #         cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            #         cv2.imshow('Frame', frame)
            #
            #         # Press Q on keyboard to  exit
            #         if cv2.waitKey(25) & 0xFF == ord('q'):
            #             break
            #
            #     # Break the loop
            #     else:
            #         break
            webcam = cv2.VideoCapture(0)
            if ipsum<=0:
                flag_thank_you=0;



        key = cv2.waitKey(1)
        if key == ord(' '):
            if flag_thank_you==0:
                check, frame = webcam.read()

                filename = 'image' + str(pictures_left) + '.jpg'
                cv2.imwrite(filename, img=frame)
                #time.sleep(.8)
                shutil.copy("/Users/Manuk/Downloads/capturing-images-from-webcam-using-opencv-python-masterreloaded/"+filename,
                            "/Users/Manuk/Downloads/photos_morph/"+filename)
                pictures_left -= 1
                flag_thank_you = 1

                if pictures_left <= 0:
                    webcam.release()
                    #img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                    #img_new = cv2.imshow("Captured Image", img_new)

                    fine=True

                # print("Processing image...")
                # img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                # print("Converting RGB image to grayscale...")
                # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                # print("Converted RGB image to grayscale...")
                # print("Resizing image to 28x28 scale...")
                # img_ = cv2.resize(gray, (int(1280/2), int(720/2)))
                # print("Resized...")
                # img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                # print("Image saved!")


        
    except KeyboardInterrupt:
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

webcam.release()

cv2.waitKey(1650)
cv2.destroyWindow("Capturing")
cv2.destroyAllWindows()
# os.execv('/Users/Manuk/Downloads/face_morpher-dlib/facemorpher/purpose.py', ('/Users/Manuk/Downloads/face_morpher-dlib/facemorpher/purpose.py', '--principale=/Users/Manuk/Downloads/photos_morph', '--secondario=/Users/Manuk/Downloads/images_morph2_intermediate', '--A=/Users/Manuk/Downloads/images_morph2/A', '--B=/Users/Manuk/Downloads/images_morph2/B', '--C=/Users/Manuk/Downloads/images_morph2/C', '--destinazione=/Users/Manuk/Downloads/morphdef.avi'))
# os.system(exit(28))
# os.system(
#     'python3 /Users/Manuk/Downloads/face_morpher-dlib/facemorpher/purpose.py --principale=/Users/Manuk/Downloads/photos_morph --secondario=/Users/Manuk/Downloads/images_morph2_intermediate --A=/Users/Manuk/Downloads/images_morph2/A --B=/Users/Manuk/Downloads/images_morph2/B --C=/Users/Manuk/Downloads/images_morph2/C --destinazione=/Users/Manuk/Downloads/morphdef.avi')
