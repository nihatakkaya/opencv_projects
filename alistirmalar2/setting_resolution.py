import cv2  # OpenCV kütüphanesini içe aktarıyoruz.

# Pencere adı belirliyoruz.
windowName = "Live Video"  # Pencerenin başlığını "Live Video" olarak belirliyoruz.
cv2.namedWindow(windowName)  # OpenCV ile bir pencere oluşturuyoruz.

# Kamerayı başlatıyoruz.
cap = cv2.VideoCapture(0)  # Bilgisayarın varsayılan kamerasını açıyoruz.

# Mevcut genişlik ve yükseklik değerlerini ekrana yazdırıyoruz.
print("Width : " + str(cap.get(3)))  # Varsayılan genişliği alıyoruz (3 = FRAME_WIDTH).
print("Height : " + str(cap.get(4)))  # Varsayılan yüksekliği alıyoruz (4 = FRAME_HEIGHT).

# Kamera çözünürlüğünü 1280x720 olarak ayarlıyoruz.
cap.set(3, 1280)  # Kameranın genişlik değerini 1280 piksel olarak ayarlıyoruz.
cap.set(4, 720)  # Kameranın yükseklik değerini 720 piksel olarak ayarlıyoruz.

# Güncellenmiş genişlik ve yükseklik değerlerini ekrana yazdırıyoruz.
print("Width* : " + str(cap.get(3)))  # Güncellenmiş genişliği alıp ekrana yazdırıyoruz.
print("Height* : " + str(cap.get(4)))  # Güncellenmiş yüksekliği alıp ekrana yazdırıyoruz.

# Sonsuz döngü içinde kameradan görüntü almaya başlıyoruz.
while True:
    _, frame = cap.read()  # Kameradan bir kare okuyoruz.

    frame = cv2.flip(frame, 1)  # Aynalama işlemi yaparak görüntüyü soldan sağa çeviriyoruz.

    cv2.imshow(windowName, frame)  # Kameradan gelen görüntüyü "Live Video" penceresinde gösteriyoruz.

    if cv2.waitKey(1) == 27:  # Kullanıcı "ESC" tuşuna (27) basarsa döngüden çıkıyoruz.
        break

# Kamera bağlantısını serbest bırakıyoruz.
cap.release()

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
