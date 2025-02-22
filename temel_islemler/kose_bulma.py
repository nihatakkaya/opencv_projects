import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# "klonasker.jpg" adlı görüntüyü okur
img1 = cv2.imread("klonasker.jpg")
img1=cv2.resize(img1,(1000,720))

# Görüntünün yüklenip yüklenmediğini kontrol et
if img1 is None:
    print("Hata: Görüntü dosyası bulunamadı veya okunamadı!")
    exit()

# Görüntüyü gri tonlamaya çevirir
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü float32 veri tipine dönüştürür
gray = np.float32(gray)

# Köşe tespiti yapar
corners = cv2.goodFeaturesToTrack(gray, 500, 0.05, 5)

# Köşe tespiti başarısızsa programı sonlandır
if corners is None:
    print("Hata: Köşe tespiti başarısız! Parametreleri kontrol edin.")
    exit()

# Köşe noktalarını tam sayıya dönüştürür
corners = corners.astype(int)

# Köşe noktalarına kırmızı daireler çizer
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 3, (0, 0, 255), -1)

# Köşe tespiti yapılan görüntüyü ekranda gösterir
cv2.imshow("corner", img1)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
