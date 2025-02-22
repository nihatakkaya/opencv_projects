# Histogram, bir görüntüdeki piksel yoğunluğunun (parlaklık seviyelerinin) dağılımını gösteren grafiksel bir temsildir.

import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır
from matplotlib import pyplot as plt  # Histogramı çizdirmek için Matplotlib kütüphanesini içe aktarır

# "klonasker.jpg" adlı görüntüyü okur
img = cv2.imread("klonasker.jpg")
img=cv2.resize(img,(1000,720))

# Görüntüyü BGR (Mavi, Yeşil, Kırmızı) kanallarına ayırır
b, g, r = cv2.split(img)

# Orijinal görüntüyü ekranda gösterir
cv2.imshow("img", img)

# Histogram hesaplama ve çizdirme işlemi
# - b.ravel() → Mavi kanalın tüm piksel değerlerini tek bir diziye dönüştürür.
# - plt.hist(b.ravel(), 256, [0, 256]) → Mavi kanal için histogram oluşturur.
# - plt.hist(g.ravel(), 256, [0, 256]) → Yeşil kanal için histogram oluşturur.
# - 256 → Piksel değerlerinin 0-255 aralığında olduğunu belirtir.
# - plt.show() → Histogramı ekrana çizer.
plt.hist(b.ravel(), 256, [0, 256], color='blue', alpha=0.5, label='Mavi')  # Mavi kanal histogramı
plt.hist(g.ravel(), 256, [0, 256], color='green', alpha=0.5, label='Yeşil')  # Yeşil kanal histogramı
plt.hist(r.ravel(), 256, [0, 256], color='red', alpha=0.5, label='Kırmızı')  # Kırmızı kanal histogramı
plt.legend()  # Renk kanallarını belirten etiketi ekler
plt.xlabel("Piksel Değerleri")  # X eksenini açıklar
plt.ylabel("Frekans")  # Y eksenini açıklar
plt.title("Görüntü Histogramı")  # Histogram başlığı
plt.show()  # Histogramı ekrana çizer

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()