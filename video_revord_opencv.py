import numpy as np
import cv2
# To load video from camera
capture = cv2.VideoCapture(0)
# To define video codec format
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# To define video writer variable
output = cv2.VideoWriter('output_video.avi', fourcc, 25, (640,480)) # 3. parameter is fps, 4. parameter is video frame size.
while(capture.isOpened()): #To check if the camera is turned on.
 ret, frame =  capture.read()
 image = cv2.rotate(frame, cv2.cv2.ROTATE_180)
 if ret == True:
     # write the image
     output.write(image)
     cv2.imshow("frame", image) # To dispay video
     if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 else:
    break
capture.release() # To release the capture
output.release() # To release the output
cv2.destroyAllWindows()