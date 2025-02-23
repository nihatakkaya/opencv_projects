import cv2  # OpenCV kütüphanesini içe aktarıyoruz.

# Trackbar değiştirildiğinde çalışacak boş bir fonksiyon tanımlıyoruz.
def nothing(x):
    pass

# İlk görüntüyü okuyoruz ve boyutunu 640x480 olarak yeniden ayarlıyoruz.
img1 = cv2.imread("7.1 balls.jpg.jpg")  # "aircraft.jpg" adlı görüntüyü okuyoruz.
img1 = cv2.resize(img1, (640, 480))  # Görüntüyü 640x480 piksel olarak yeniden boyutlandırıyoruz.

# İkinci görüntüyü okuyoruz ve boyutunu 640x480 olarak yeniden ayarlıyoruz.
img2 = cv2.imread("7.2 aircraft.jpg.jpg")  # "balls.jpg" adlı görüntüyü okuyoruz.
img2 = cv2.resize(img2, (640, 480))  # Görüntüyü 640x480 piksel olarak yeniden boyutlandırıyoruz.

# İki görüntüyü birleştiriyoruz (başlangıçta her ikisinin de ağırlığı 0.5 olarak ayarlandı).
output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# `cv2.addWeighted` fonksiyonu ile iki görüntüyü ağırlıklarına göre karıştırıyoruz.

# Pencere adını belirliyoruz.
windowName = "Transition Program"  # Pencere başlığı belirleniyor.
cv2.namedWindow(windowName)  # OpenCV ile bir pencere oluşturuyoruz.

# Alpha-Beta (geçiş oranı) için bir Trackbar oluşturuyoruz.
cv2.createTrackbar("Alpha-Beta", windowName, 0, 1000, nothing)
# 0 ile 1000 arasında değişen bir trackbar ekliyoruz.

# Sonsuz döngü ile canlı görüntü işleme başlıyor.
while True:
    cv2.imshow(windowName, output)  # Pencerede işlenmiş görüntüyü gösteriyoruz.

    # Trackbar'dan alınan değeri 1000'e bölerek alpha değerini hesaplıyoruz.
    alpha = cv2.getTrackbarPos("Alpha-Beta", windowName) / 1000
    beta = 1 - alpha  # Beta değerini hesaplıyoruz (toplam ağırlık 1 olmalı).

    # Yeni alpha ve beta değerleri ile iki görüntüyü birleştiriyoruz.
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    # Alpha ve beta değerlerine bağlı olarak görüntülerin ağırlıklarını dinamik olarak ayarlıyoruz.

    print(alpha, beta)  # Konsola güncellenen alpha ve beta değerlerini yazdırıyoruz.

    # ESC (27) tuşuna basıldığında döngüden çıkıyoruz.
    if cv2.waitKey(1) == 27:
        break

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
