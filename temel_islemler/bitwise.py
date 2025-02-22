# Bu işleçler, nesne algılama, maskeleme ve görüntü işlemede sıkça kullanılır.

import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# İki farklı görüntüyü okur ve img1 ile img2 değişkenlerine atar
img1 = cv2.imread("9.1 bitwise_2.png.png")  # İlk görüntüyü okur
img2 = cv2.imread("9.2 bitwise_1.png.png")  # İkinci görüntüyü okur

# Mantık işleçleri kullanarak görüntüler arasında işlemler gerçekleştirir

# AND işlemi: İki görüntüyü bit seviyesinde AND işlemine tabi tutar
# Siyah (0) ve beyaz (1) değerleri üzerinden mantıksal AND işlemi uygulanır
# - 0 AND 0 = 0 (Siyah)
# - 1 AND 0 = 0 (Siyah)
# - 1 AND 1 = 1 (Beyaz)
bit_and = cv2.bitwise_and(img2, img1)

# OR işlemi: İki görüntüyü bit seviyesinde OR işlemine tabi tutar
# - 0 OR 0 = 0 (Siyah)
# - 1 OR 0 = 1 (Beyaz)
# - 1 OR 1 = 1 (Beyaz)
bit_or = cv2.bitwise_or(img2, img1)

# XOR işlemi: İki görüntüyü bit seviyesinde XOR işlemine tabi tutar
# - 0 XOR 0 = 0 (Siyah)
# - 1 XOR 0 = 1 (Beyaz)
# - 1 XOR 1 = 0 (Siyah)
bit_xor = cv2.bitwise_xor(img2, img1)

# NOT işlemi: Görüntünün renklerini ters çevirir (Negatifini alır)
# Siyah olan yerler beyaza, beyaz olan yerler siyaha döner
bit_not = cv2.bitwise_not(img2)  # img2'nin negatifini alır
bit_not2 = cv2.bitwise_not(img1)  # img1'in negatifini alır

# Görüntüleri ekranda gösterir
cv2.imshow("img1", img1)  # İlk görüntüyü gösterir
cv2.imshow("img2", img2)  # İkinci görüntüyü gösterir
cv2.imshow("bit_and", bit_and)  # AND işlemine tabi tutulmuş görüntüyü gösterir
cv2.imshow("bit_or", bit_or)  # OR işlemine tabi tutulmuş görüntüyü gösterir
cv2.imshow("bit_xor", bit_xor)  # XOR işlemine tabi tutulmuş görüntüyü gösterir
cv2.imshow("bit_not", bit_not)  # img2'nin ters çevrilmiş halini gösterir
cv2.imshow("bit_not2", bit_not2)  # img1'in ters çevrilmiş halini gösterir

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
