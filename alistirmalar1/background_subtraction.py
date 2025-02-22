import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Video dosyasını açıyoruz.
cap = cv2.VideoCapture("5.1 car.mp4.mp4")  # Belirtilen video dosyasını okuyoruz.

# Arka plan çıkarma için MOG2 algoritmasını kullanıyoruz.
# - history=100: Arka plan modellemesi için kullanılan kare sayısı.
# - varThreshold=120: Hareket algılamadaki eşik değeri.
# - detectShadows=True: Gölge algılamayı aktif hale getirir.
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=120, detectShadows=True)

# Sonsuz döngü içinde videoyu kare kare işliyoruz.
while True:
    _, frame = cap.read()  # Videodan bir kare okuyoruz.

    # Eğer video bitmişse veya kare okunamıyorsa döngüyü kır.
    if frame is None:
        break

    # Okunan kareyi 640x480 boyutuna yeniden boyutlandırıyoruz.
    frame = cv2.resize(frame, (640, 480))

    # Arka plan çıkarma işlemi uyguluyoruz.
    mask = subtractor.apply(frame)

    # Orijinal videoyu ekranda gösteriyoruz.
    cv2.imshow("frame", frame)

    # Arka plan çıkarılmış (hareket algılanmış) görüntüyü ekranda gösteriyoruz.
    cv2.imshow("mask", mask)

    # 'q' tuşuna basıldığında döngüden çıkıyoruz.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Video dosyasını serbest bırakıyoruz.
cap.release()

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
