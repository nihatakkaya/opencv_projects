import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Görüntü dosyalarını okuyoruz.
img1 = cv2.imread("5.1 coins.jpg.jpg")  # İlk görüntüyü okuyoruz.
img2 = cv2.imread("5.2 balls.jpg.jpg")  # İkinci görüntüyü okuyoruz.

# Görüntüleri gri tonlamaya çeviriyoruz.
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # İlk görüntüyü gri tona çeviriyoruz.
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # İkinci görüntüyü gri tona çeviriyoruz.

# Gürültüyü azaltmak için median blur (medyan bulanıklaştırma) uyguluyoruz.
img1_blur = cv2.medianBlur(gray1, 5)  # İlk görüntüye 5x5 kernel ile bulanıklaştırma uyguluyoruz.
img2_blur = cv2.medianBlur(gray2, 5)  # İkinci görüntüye 5x5 kernel ile bulanıklaştırma uyguluyoruz.

# Hough Transform yöntemi ile daireleri tespit ediyoruz.
# Parametreler:
# - cv2.HOUGH_GRADIENT: Hough dönüşüm metodu.
# - 1: Parametre olarak kullanılan dp değeri (görüntü çözünürlüğü ölçeklendirme faktörü).
# - img2.shape[0]/4: Minumum mesafe (yarıçap mesafesi).
# - param1=200: Canny kenar algılama için üst eşik değeri.
# - param2=10: Daire tespiti için gereken minimum oy sayısı (daha yüksek değerler daha az ama kesin sonuçlar verir).
# - minRadius=10, maxRadius=100: Minimum ve maksimum daire yarıçapı.
circles = cv2.HoughCircles(img2_blur, cv2.HOUGH_GRADIENT, 1, img2.shape[0] / 4, param1=200, param2=10, minRadius=10,
                           maxRadius=100)

# Eğer daireler tespit edildiyse işleme devam et.
if circles is not None:
    circles = np.uint16(np.around(circles))  # Daire koordinatlarını tamsayıya yuvarlıyoruz.

    # Tespit edilen her daireyi çiziyoruz.
    for i in circles[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Daireleri yeşil renk ve 2 piksel kalınlıkla çiziyoruz.

# Orijinal görüntüyü ekranda gösteriyoruz.
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("gray1", gray1)
cv2.imshow("gray2", gray2)
cv2.imshow("blur1", img1_blur)
cv2.imshow("blur2", img2_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

