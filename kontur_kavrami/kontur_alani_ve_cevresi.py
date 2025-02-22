import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "5.1 contour.png.png" adlı görüntüyü okur
img = cv2.imread("5.1 contour.png.png")

# Görüntüyü gri tonlamaya çevirir
# - cv2.COLOR_BGR2GRAY: Renkli görüntüyü siyah-beyaz hale getirir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# İkili (binary) eşikleme uygular
# - 127: Eşik değeri
# - 255: Maksimum piksel değeri (beyaz)
# - cv2.THRESH_BINARY: Piksel değeri 127'den büyükse 255 (beyaz), küçükse 0 (siyah) yapar
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Görüntüdeki konturları (sınırları) bulur
# - cv2.RETR_TREE: Tüm kontur hiyerarşisini çıkarır
# - cv2.CHAIN_APPROX_SIMPLE: Gereksiz noktaları kaldırarak sadece gerekli köşe noktalarını saklar
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# İlk konturu seçer
cnt = contours[0]

# Konturun alanını hesaplar
area = cv2.contourArea(cnt)
print("Kontur Alanı:", area)

# Konturun momentlerini hesaplar
M = cv2.moments(cnt)
print("Moment m00 (alan):", M['m00'])

# Konturun çevresini (perimeter) hesaplar
# - True: Konturun kapalı olduğunu belirtir
perimeter = cv2.arcLength(cnt, True)
print("Kontur Çevresi:", perimeter)

# Görüntüleri ekranda gösterir
cv2.imshow("original", img)  # Orijinal görüntüyü gösterir
cv2.imshow("gray", gray)  # Gri tonlamalı görüntüyü gösterir
cv2.imshow("thresh", thresh)  # Eşiklenmiş görüntüyü gösterir

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()