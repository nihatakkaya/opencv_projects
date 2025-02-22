import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255
#print(canvas)

cv2.line(canvas, (50,50),(512,512),(255,0,0),thickness=5)
cv2.line(canvas, (100,50),(200,250),(0,0,255),thickness=7)

cv2.rectangle(canvas, (100,100),(300,300),(0,255,0),thickness=-1)

cv2.circle(canvas, (250,250),100,(0,0,255),thickness=5)

p1= (100,200)
p2= (50,50)
p3= (300,100)

cv2.line(canvas, p1, p2, (0,0,0),4)
cv2.line(canvas, p2, p3, (0,0,0),4)
cv2.line(canvas, p1, p3, (0,0,0),4)

points = np.array([[110,200],[330,200],[290,220],[220,250]], np.int32)
cv2.polylines(canvas,[points], True, (0,0,100),5)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

