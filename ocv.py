import cv2 as cv
import numpy as np

img = cv.imread('hallway.jpg')


scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
frame = cv.resize(img, dim, interpolation = cv.INTER_AREA)

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)
can = cv.Canny(blur, 35,100)
lines = cv.HoughLinesP(can, 2, np.pi/180, 100, np.array([]), minLineLength=50, maxLineGap=10)

line_overlay = np.zeros_like(frame)
for line in lines:
	x1, y1, x2, y2 = line.reshape(4)
	a = (y2 - y1) / (x2 - x1)
	a = np.sinh(a)/np.cosh(a)
	if a != 'inf':
		if a != '-inf':
			if not (-0.3 <= a <= 0.3):
				if(-0.7 <= a <= 0.7):

					cv.line(line_overlay, (x1, y1), (x2, y2), (0, 255, 00), 3)
					print(a)

combo = cv.addWeighted(frame, 0.8, line_overlay, 1.0, 1)
#cv.imshow('gray', frame)
cv.imshow('result', combo)

cv.waitKey(0)

#cap.release()
cv.destroyAllWindows()


