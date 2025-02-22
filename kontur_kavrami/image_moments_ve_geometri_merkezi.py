import cv2  # OpenCV kütüphanesini içe aktarır

# Görüntüyü dosyadan okur
img = cv2.imread('5.1 contour.png.png')

# Görüntüyü gri tonlamaya çevirir
# - cv2.COLOR_BGR2GRAY: Renkli görüntüyü siyah-beyaz hale getirir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# İkili (binary) eşikleme uygular
# - 127: Eşik değeri
# - 255: Maksimum piksel değeri (beyaz)
# - cv2.THRESH_BINARY: Piksel değeri 127'den büyükse 255 (beyaz), küçükse 0 (siyah) yapar
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Görüntünün momentlerini hesaplar
# - Momentler, görüntüdeki konturları ve merkezleri belirlemek için kullanılır
M = cv2.moments(thresh)

# Görüntünün ağırlık merkezini hesaplar
# - M["m10"] ve M["m01"]: Moment değerleri
# - M["m00"]: Alanı ifade eder
# - Eğer alan sıfır değilse, X ve Y koordinatlarını hesaplar
if M["m00"] != 0:
    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])
    # Ağırlık merkezine yeşil bir daire çizer
    cv2.circle(img, (X, Y), 5, (0, 255, 0), -1)

# Görüntüyü ekranda gösterir
cv2.imshow("img", img)

# Kullanıcıdan bir tuşa basmasını bekler
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
