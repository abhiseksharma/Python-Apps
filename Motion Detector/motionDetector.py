import cv2, time
from datetime import datetime

video = cv2.VideoCapture(0)

first_frame = None
status_list = [None, None]
times = []


while True:
	check, frame = video.read()
	status = 0

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21,21),0)

	if first_frame is None:
		first_frame = gray
		#continue

	diff = cv2.absdiff(first_frame, gray)

	thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations = 2)

	(_, cnts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in cnts:
		if cv2.contourArea(contour) < 1000:
			continue
		status = 1
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(gray, (x ,y), (x+w, y+h), (0,255,0), 3)
	status_list.append(status)

	if status_list[-1] == 1 and status_list[-2] == 0:
		times.append(datetime.now())
	if status_list[-1] == 0 and status_list[-2] == 1:
		times.append(datetime.now())

	cv2.imshow('name', gray)
	cv2.imshow('Diff', diff)
	cv2.imshow('Thresh',  thresh)

	key = cv2.waitKey(1)

	if key==ord('q'):
		break
print(times)
video.release()
cv2.destroyAllWindows()