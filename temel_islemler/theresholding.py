"""Thresholding, bir görüntüdeki piksel değerlerini belirli bir eşik değere göre değiştirme işlemidir.
Genellikle görüntüyü ikili (binary) hale getirmek, yani sadece siyah ve beyaz piksellerden oluşan bir görüntü elde etmek için kullanılır."""

import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır
from matplotlib import pyplot as plt  # Görüntüleri çizdirmek için Matplotlib kütüphanesini içe aktarır

# "klon.jpg" adlı görüntüyü gri tonlamalı olarak okur
img = cv2.imread("klonasker.jpg", 0)
img=cv2.resize(img,(1000,720))


# Basit eşikleme yöntemi uygular
# - 150: Eşik değeri
# - 200: Maksimum piksel değeri (beyaz)
# - cv2.THRESH_BINARY: Piksel değeri eşik değerinden büyükse 200 (beyaz), değilse 0 (siyah) yapar
ret, th1 = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)

# Adaptif ortalama eşikleme yöntemi uygular
# - 255: Maksimum piksel değeri
# - cv2.ADAPTIVE_THRESH_MEAN_C: Yerel alan ortalamasına göre eşikleme yapar
# - cv2.THRESH_BINARY: İkili eşikleme uygular
# - 21: Çekirdek boyutu (blok büyüklüğü)
# - 2: Sabit değer, eşikten çıkarılır
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)

# Adaptif Gauss eşikleme yöntemi uygular
# - cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Gaussian ağırlıklı ortalama kullanır
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

# Eşiklenmiş görüntüleri ekranda gösterir
cv2.imshow("img-th1", th1)  # Basit eşikleme yöntemiyle elde edilen görüntü
cv2.imshow("img-th2", th2)  # Adaptif ortalama eşikleme yöntemiyle elde edilen görüntü
cv2.imshow("img-th3", th3)  # Adaptif Gauss eşikleme yöntemiyle elde edilen görüntü

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()