'''
Author: Ezekiel A. Mitchell
Creation date: 21 August 2024
Last modified: 21 August 2024
-----------------------------
About: This script utilizes opencv to activate either the PI camera module [0] 
or the usb camera [2].

Notes:
- The index for the usb camera will vary on which usb port is being used.
'''

import cv2

cap = cv2.VideoCapture(2)

while True:
	ret, frame = cap.read()
	
	frame1 = cv2.flip(frame, 1)
	
	cv2.imshow('Frame', frame1)
	
	if cv2.waitKey(1) == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
