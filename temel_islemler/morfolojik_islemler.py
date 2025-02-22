import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı görüntüyü gri tonlamalı olarak okur
img = cv2.imread("klonasker.jpg", 0)
img=cv2.resize(img,(1000,720))

# 5x5 boyutunda tüm elemanları 1 olan bir çekirdek (kernel) matrisi oluşturur
# np.uint8 veri tipi, piksellerin 0-255 arasında değerler almasını sağlar
kernel = np.ones((5,5), np.uint8)

# Tophat dönüşümü uygular
# - cv2.MORPH_TOPHAT: Orijinal görüntü ile açma (erosion + dilation) işlemi sonrası farkı alır
# - Küçük parlak detayları öne çıkarmak için kullanılır
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Orijinal görüntüyü ekranda gösterir
cv2.imshow("img", img)

# Tophat dönüşümü sonucu oluşan görüntüyü ekranda gösterir
cv2.imshow("TOPHAT", tophat)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
