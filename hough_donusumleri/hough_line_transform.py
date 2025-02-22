import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Görüntüyü okumak için OpenCV'nin imread fonksiyonunu kullanıyoruz.
img = cv2.imread("3.1 h_line.png.png")

# Görüntüyü gri tonlamaya çeviriyoruz (BGR'den GRAY'e dönüşüm).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kenar tespiti için Canny algoritmasını kullanıyoruz.
# 75 ve 150 eşik değerleri ile kenarları belirliyoruz.
edges = cv2.Canny(gray, 75, 150)

# Hough Line Transform'u kullanarak doğruları tespit ediyoruz.
# Parametreler:
# - 1: Rho çözünürlüğü (piksel cinsinden).
# - np.pi/180: Açı çözünürlüğü (radyan cinsinden).
# - 50: Bir doğruyu oluşturmak için gereken minimum oylama sayısı.
# - maxLineGap=200: Bir doğruyu oluşturan maksimum kesinti uzunluğu.
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200)

# Bulunan çizgileri görüntü üzerine çiziyoruz.
for line in lines:
    (x1, y1, x2, y2) = line[0]  # Çizginin başlangıç ve bitiş koordinatlarını alıyoruz.
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Yeşil renkli (0,255,0) ve 2 piksel kalınlığında çiziyoruz.

# Orijinal görüntüyü ekranda gösteriyoruz.
cv2.imshow("img", img)

# Gri tonlamalı görüntüyü ekranda gösteriyoruz.
cv2.imshow("gray", gray)

# Kenar tespiti yapılmış görüntüyü ekranda gösteriyoruz.
cv2.imshow("edges", edges)

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
