import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı görüntüyü gri tonlamalı olarak okur
img = cv2.imread("klonasker.jpg", 0)

# Görüntünün satır (row) ve sütun (col) boyutlarını alır
row, col = img.shape

# Döndürme matrisi oluşturulur
# - (col/5, row/3): Döndürme merkezi belirlenir
# - 180: Görüntü 180 derece döndürülür
# - 1: Ölçek faktörü (1, boyutu değiştirmeden döndürür)
M = cv2.getRotationMatrix2D((col/5, row/3), 180, 1)

# cv2.warpAffine() fonksiyonu ile görüntü döndürme işlemi uygulanır
# - img: Giriş görüntüsü
# - M: Döndürme matrisi
# - (col, row): Çıktı görüntüsünün boyutu
dst = cv2.warpAffine(img, M, (col, row))

# Döndürülmüş görüntüyü ekranda gösterir
cv2.imshow("dst", dst)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
