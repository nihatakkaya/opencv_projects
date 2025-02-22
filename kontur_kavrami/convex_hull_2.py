import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Görüntüyü okumak için OpenCV'nin imread fonksiyonunu kullanıyoruz.
img = cv2.imread("8.1 map.jpg.jpg")

# Görüntüyü gri tonlamaya çeviriyoruz (BGR'den GRAY'e dönüşüm).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için görüntüye bulanıklaştırma filtresi uyguluyoruz.
blur = cv2.blur(gray, (3,3))

# Görüntüye eşikleme (thresholding) uyguluyoruz.
# 40'ın altındaki pikseller siyah (0), 40'ın üzerindekiler beyaz (255) olacak şekilde ikili bir görüntü oluşturuyoruz.
ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)

# Görüntüdeki nesnelerin dış hatlarını (contours) ve hiyerarşisini belirliyoruz.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dış hatların dışbükey zarflarını (convex hull) tutmak için boş bir liste oluşturuyoruz.
hull = []

# Her bir konturun dışbükey zarfını hesaplayıp listeye ekliyoruz.
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

# Boş bir siyah arka plan görüntüsü oluşturuyoruz.
bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# Bulunan konturları ve dışbükey zarfları çiziyoruz.
for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (255, 0, 0), 3, 8)  # Mavi renkte konturları çiziyoruz.
    cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 8)  # Yeşil renkte dışbükey zarfı çiziyoruz.

# İşlenmiş görüntüyü ekranda gösteriyoruz.
cv2.imshow("Image", bg)

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
