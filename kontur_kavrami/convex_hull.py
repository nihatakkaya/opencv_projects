import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "8.1 map.jpg.jpg" adlı görüntüyü okur
img = cv2.imread("8.1 map.jpg.jpg")

# Görüntünün boyutunu 1000x720 piksel olarak yeniden boyutlandırır
img = cv2.resize(img, (1000, 720))

# Görüntüyü gri tonlamaya çevirir
# - cv2.COLOR_BGR2GRAY: Renkli görüntüyü siyah-beyaz hale getirir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüye bulanıklık filtresi uygular
# - (3,3): 3x3 boyutunda bir çekirdek (kernel) kullanarak bulanıklaştırma yapar
blur = cv2.blur(gray, (3, 3))

# İkili (binary) eşikleme uygular
# - 75: Eşik değeri
# - 255: Maksimum piksel değeri (beyaz)
# - cv2.THRESH_BINARY: Piksel değeri 75'ten büyükse 255 (beyaz), küçükse 0 (siyah) yapar
ret, thresh = cv2.threshold(blur, 75, 255, cv2.THRESH_BINARY)

# Orijinal görüntüyü ekranda gösterir
cv2.imshow("original", img)

# Gri tonlamalı görüntüyü ekranda gösterir
cv2.imshow("gray", gray)

# Bulanıklaştırılmış görüntüyü ekranda gösterir
cv2.imshow("blur", blur)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
