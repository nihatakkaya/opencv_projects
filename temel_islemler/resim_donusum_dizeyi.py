import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı görüntüyü gri tonlamalı olarak okur
img = cv2.imread("klonasker.jpg", 0)
img=cv2.resize(img,(1000,720))

# Görüntünün satır (row) ve sütun (col) boyutlarını alır
row, col = img.shape

# Öteleme (translation) matrisi oluşturulur
# X ekseninde 50 piksel sağa, Y ekseninde 200 piksel aşağı kaydırma yapılır
M = np.float32([[1, 0, 50], [0, 1, 200]])

# cv2.warpAffine() fonksiyonu ile görüntü öteleme işlemi uygulanır
# - img: Giriş görüntüsü
# - M: Öteleme matrisi
# - (row, col): Çıktı görüntüsünün boyutu
# Sonuç olarak, dst değişkenine kaydırılmış yeni görüntü atanır
dst = cv2.warpAffine(img, M, (row, col))

# Ötelenmiş görüntüyü ekranda gösterir
cv2.imshow("dst", dst)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
