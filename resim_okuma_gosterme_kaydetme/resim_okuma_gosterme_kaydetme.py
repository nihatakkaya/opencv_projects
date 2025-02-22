import cv2

img= cv2.imread("../temel_islemler/klonasker.jpg")
#print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("İmage",img)
cv2.imwrite("klon1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()






