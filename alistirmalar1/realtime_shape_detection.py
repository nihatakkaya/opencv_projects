import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Trackbar için boş bir fonksiyon tanımlıyoruz.
def nothing(x):
    pass

# Kamerayı başlatıyoruz.
cap = cv2.VideoCapture(0)  # Bilgisayarın varsayılan kamerasını açıyoruz.

# "Settings" adlı bir pencere oluşturuyoruz.
cv2.namedWindow("Settings")

# Renk eşikleme (threshold) değerlerini ayarlamak için Trackbar (kaydırma çubuğu) oluşturuyoruz.
cv2.createTrackbar("Lower-Hue", "Settings", 0, 180, nothing)  # Alt Hue değeri
cv2.createTrackbar("Lower-Saturation", "Settings", 0, 255, nothing)  # Alt Doygunluk (Saturation) değeri
cv2.createTrackbar("Lower-Value", "Settings", 0, 255, nothing)  # Alt Parlaklık (Value) değeri
cv2.createTrackbar("Upper-Hue", "Settings", 0, 180, nothing)  # Üst Hue değeri
cv2.createTrackbar("Upper-Saturation", "Settings", 0, 255, nothing)  # Üst Doygunluk değeri
cv2.createTrackbar("Upper-Value", "Settings", 0, 255, nothing)  # Üst Parlaklık değeri

# Yazı tipi ayarlıyoruz.
font = cv2.FONT_HERSHEY_SIMPLEX  # OpenCV içinde bulunan basit yazı tipi.

# Sonsuz döngü içinde sürekli görüntü alıyoruz.
while True:
    ret, frame = cap.read()  # Kameradan bir kare okuyoruz.

    # Aynadaki gibi görüntü ters olmasın diye çeviriyoruz.
    frame = cv2.flip(frame, 1)

    # BGR formatındaki görüntüyü HSV renk uzayına çeviriyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan alt ve üst renk eşikleme değerlerini alıyoruz.
    lh = cv2.getTrackbarPos("Lower-Hue", "Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation", "Settings")
    lv = cv2.getTrackbarPos("Lower-Value", "Settings")
    uh = cv2.getTrackbarPos("Upper-Hue", "Settings")
    us = cv2.getTrackbarPos("Upper-Saturation", "Settings")
    uv = cv2.getTrackbarPos("Upper-Value", "Settings")

    # Renk eşik değerlerini NumPy dizisi olarak tanımlıyoruz.
    lower_color = np.array([lh, ls, lv])  # Alt eşik değeri
    upper_color = np.array([uh, us, uv])  # Üst eşik değeri

    # HSV görüntüde belirlenen renk aralığını maskeleme işlemiyle filtreliyoruz.
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Gürültü azaltmak için erozyon (erode) işlemi uyguluyoruz.
    kernel = np.ones((5, 5), np.uint8)  # 5x5 boyutunda bir kernel (çekirdek) oluşturuyoruz.
    mask = cv2.erode(mask, kernel)  # Maske üzerinde erozyon işlemi uyguluyoruz.

    # Konturları (nesne sınırlarını) buluyoruz.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Tespit edilen her konturu döngüyle işliyoruz.
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Konturun alanını hesaplıyoruz.

        # Konturun kenarlarını belirlemek için basitleştirilmiş bir çokgen oluşturuyoruz.
        epsilon = 0.02 * cv2.arcLength(cnt, True)  # Konturun uzunluğunun %2'si kadar hata toleransı belirliyoruz.
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # Köşe noktalarını belirleyerek şekli sadeleştiriyoruz.

        # İlk noktanın koordinatlarını alıyoruz.
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # Eğer alan 400 pikselden büyükse (çok küçük nesneleri filtrelemek için)
        if area > 400:
            # Konturları çiziyoruz.
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            # Şeklin kaç kenarı olduğunu kontrol ederek adını belirtiyoruz.
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))  # Üçgen

            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))  # Dörtgen

            elif len(approx) > 6:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))  # Daire

    # Gerçek zamanlı işlemleri göstermek için görüntüleri ekranda gösteriyoruz.
    cv2.imshow("frame", frame)  # Kameradan gelen işlenmiş görüntü.
    cv2.imshow("mask", mask)  # Filtrelenen renklerin maskesi.

    # Klavyeden 'q' tuşuna basıldığında döngüyü sonlandır.
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırakıyoruz ve pencereleri kapatıyoruz.
cap.release()
cv2.destroyAllWindows()
