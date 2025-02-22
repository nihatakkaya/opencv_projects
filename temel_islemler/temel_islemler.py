import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı resmi okur ve img değişkenine atar
img = cv2.imread("klonasker.jpg")

# Görüntünün boyutlarını (yükseklik, genişlik, kanal sayısı) alır
dimension = img.shape
print(dimension)  # Boyut bilgilerini ekrana yazdırır

# Belirtilen piksel koordinatındaki (150, 200) renk değerlerini alır
color = img[150,200]
print(color)  # Pikselin BGR (Mavi, Yeşil, Kırmızı) değerlerini ekrana yazdırır

# Belirtilen piksel koordinatındaki (420, 500) mavi (0. kanal) bileşeni alır
blue = img[420, 500, 0]
print(blue)  # Mavi bileşenin değerini ekrana yazdırır

# Görüntüyü yeni bir boyuta (1000x720 piksel) yeniden boyutlandırır
img=cv2.resize(img,(1000,720))

# Yeniden boyutlandırılmış görüntüyü "Klon Asker" başlıklı bir pencere içinde gösterir
cv2.imshow("Klon Asker", img)

# Kullanıcıdan bir tuşa basmasını bekler ve ardından devam eder
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
