import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('news.jpg', 0)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(image, scaleFactor = 1.08, minNeighbors = 5)

for x,y,w,h in face:
	image = cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 3)

cv2.imshow('name', image)
cv2.waitKey(0)
cv2.destroyAllWindows()