import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı resmi okur ve img değişkenine atar
img = cv2.imread("klonasker.jpg")

# Görüntüyü yeni bir boyuta (640x426 piksel) yeniden boyutlandırır
img = cv2.resize(img, (640, 426))

# ROI (Region of Interest - İlgi Alanı) belirleme
# Görüntünün 30'dan 200. piksele kadar olan satırlarını (yükseklik),
# 200'den 400. piksele kadar olan sütunlarını (genişlik) alır
roi = img[30:200, 200:400]

# Yeniden boyutlandırılmış görüntüyü "Klon" başlıklı bir pencere içinde gösterir
cv2.imshow("Klon", img)

# ROI (ilgi alanı) görüntüsünü "ROI" başlıklı bir pencere içinde gösterir
cv2.imshow("ROI", roi)

# Kullanıcıdan bir tuşa basmasını bekler ve ardından devam eder
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
