import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# Kameradan görüntü almak için VideoCapture nesnesi oluşturur
webcam = cv2.VideoCapture(0)  # 0, varsayılan web kamerayı temsil eder

def nothing(x):  # Trackbar için boş bir callback fonksiyonu oluşturur
    pass

# Trackbar için bir pencere oluşturur
cv2.namedWindow("Trackbar")

# Trackbar penceresini 500x500 piksel boyutuna ayarlar
cv2.resizeWindow("Trackbar", 500, 500)

# Trackbar'ları oluşturur (HSV renk uzayı için alt ve üst sınırlar)
cv2.createTrackbar("altsınır-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("altsınır-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("altsınır-V", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("üstsınır-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("üstsınır-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("üstsınır-V", "Trackbar", 0, 255, nothing)

# Trackbar'ların başlangıç değerlerini ayarlar
cv2.setTrackbarPos("üstsınır-H", "Trackbar", 180)
cv2.setTrackbarPos("üstsınır-S", "Trackbar", 255)
cv2.setTrackbarPos("üstsınır-V", "Trackbar", 255)

# Kameradan sürekli olarak görüntü almak için döngü başlatır
while True:
    ret, frame = webcam.read()  # Kameradan bir kare okur
    frame = cv2.flip(frame, 1)  # Aynada gördüğümüz gibi görüntüyü yatay çevirir

    # Görüntüyü HSV renk uzayına dönüştürür
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'dan alınan değerleri okur
    altsinir_h = cv2.getTrackbarPos("altsınır-H", "Trackbar")
    altsinir_s = cv2.getTrackbarPos("altsınır-S", "Trackbar")
    altsinir_v = cv2.getTrackbarPos("altsınır-V", "Trackbar")
    ustsinir_h = cv2.getTrackbarPos("üstsınır-H", "Trackbar")
    ustsinir_s = cv2.getTrackbarPos("üstsınır-S", "Trackbar")
    ustsinir_v = cv2.getTrackbarPos("üstsınır-V", "Trackbar")

    # Alt ve üst renk sınırlarını bir NumPy dizisine çevirir
    alt_color = np.array([altsinir_h, altsinir_s, altsinir_v])
    ust_color = np.array([ustsinir_h, ustsinir_s, ustsinir_v])

    # Belirlenen renk aralığında kalan pikselleri beyaz, diğerlerini siyah gösteren maske oluşturur
    mask = cv2.inRange(frame_hsv, alt_color, ust_color)

    # Orijinal görüntüyü ve maskeyi ekranda gösterir
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    # Kullanıcı "q" tuşuna basarsa döngüden çıkar
    if cv2.waitKey(20) % 0xFF == ord("q"):
        break

# Kamerayı serbest bırakır
webcam.release()

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
