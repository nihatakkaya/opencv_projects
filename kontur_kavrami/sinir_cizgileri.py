import cv2  # OpenCV kütüphanesini içe aktarır

# "2.1 contour1.png.png" adlı görüntüyü okur
img = cv2.imread("2.1 contour1.png.png")

# Görüntüyü gri tonlamaya çevirir
# - cv2.COLOR_BGR2GRAY: Renkli görüntüyü siyah-beyaz hale getirir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# İkili (binary) eşikleme uygular
# - 127: Eşik değeri
# - 255: Maksimum piksel değeri (beyaz)
# - cv2.THRESH_BINARY: Piksel değeri 127'den büyükse 255 (beyaz), küçükse 0 (siyah) yapar
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Görüntüdeki konturları (sınırları) bulur
# - cv2.RETR_TREE: Tüm kontur hiyerarşisini çıkarır
# - cv2.CHAIN_APPROX_SIMPLE: Gereksiz noktaları kaldırarak sadece gerekli köşe noktalarını saklar
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1,(0,0,255),3)

cv2.imshow("contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
