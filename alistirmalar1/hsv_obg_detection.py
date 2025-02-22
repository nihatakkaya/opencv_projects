import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Trackbar için boş bir fonksiyon tanımlıyoruz. (Trackbar değiştiğinde çağrılan fonksiyon)
def nothing(x):
    pass

# Video dosyasını açıyoruz.
cap = cv2.VideoCapture("7.1 hsv.mp4.mp4")  # Belirtilen video dosyasını okuyoruz.

# "Trackbar" adlı bir pencere oluşturuyoruz.
cv2.namedWindow("Trackbar")

# Renk eşikleme (HSV değerlerini belirlemek) için Trackbar (kaydırma çubuğu) oluşturuyoruz.
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)  # Alt Hue (renk tonu) değeri için trackbar
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)  # Alt Saturation (doygunluk) değeri için trackbar
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)  # Alt Value (parlaklık) değeri için trackbar
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)  # Üst Hue (renk tonu) değeri için trackbar
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)  # Üst Saturation (doygunluk) değeri için trackbar
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)  # Üst Value (parlaklık) değeri için trackbar

# Sonsuz döngü içinde videoyu kare kare işliyoruz.
while True:
    ret, frame = cap.read()  # Videodan bir kare okuyoruz.

    # Eğer video sonuna gelindiyse veya kare okunamadıysa döngüyü atla.
    if ret is False:
        continue  # Hata oluşmasını önlemek için döngüyü devam ettiriyoruz.

    # Okunan kareyi 500x350 boyutuna yeniden boyutlandırıyoruz.
    frame = cv2.resize(frame, (500, 350))

    # BGR formatındaki görüntüyü HSV renk uzayına çeviriyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan alınan renk eşikleme değerlerini okuyoruz.
    lh = cv2.getTrackbarPos("LH", "Trackbar")  # Alt Hue değeri
    ls = cv2.getTrackbarPos("LS", "Trackbar")  # Alt Saturation değeri
    lv = cv2.getTrackbarPos("LV", "Trackbar")  # Alt Value değeri
    uh = cv2.getTrackbarPos("UH", "Trackbar")  # Üst Hue değeri
    us = cv2.getTrackbarPos("US", "Trackbar")  # Üst Saturation değeri
    uv = cv2.getTrackbarPos("UV", "Trackbar")  # Üst Value değeri

    # HSV renk aralıklarını NumPy dizisi olarak tanımlıyoruz.
    lower_blue = np.array([lh, ls, lv])  # Alt renk eşiği
    upper_blue = np.array([uh, us, uv])  # Üst renk eşiği

    # Belirlenen HSV aralığında maskelenmiş görüntü oluşturuyoruz.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskeyi kullanarak yalnızca seçili renk aralığını içeren bir görüntü oluşturuyoruz.
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal videoyu ekranda gösteriyoruz.
    cv2.imshow("frame", frame)

    # Maske uygulanmış görüntüyü ekranda gösteriyoruz (sadece belirlenen renkteki alanlar beyaz, diğerleri siyah).
    cv2.imshow("mask", mask)

    # Maske uygulanmış ve renkle birleşmiş görüntüyü ekranda gösteriyoruz.
    cv2.imshow("bitwise", bitwise)

    # 'q' tuşuna basıldığında döngüden çıkıyoruz.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Video dosyasını serbest bırakıyoruz.
cap.release()

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
