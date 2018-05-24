import cv2
import glob

listy = glob.glob('*.jpg')

for i in listy:
	image = cv2.imread(i, 1)
	image = cv2.resize(image, (image.shape[1]//2,image.shape[0]//2))
	cv2.imshow('Galaxy', image)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()