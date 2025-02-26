import cv2
import numpy as np

def nothing(x):
    pass

# Kamerayı başlatıyoruz
cap = cv2.VideoCapture(0)

# "Trackbars" adlı bir pencere oluşturuyoruz.
cv2.namedWindow("Trackbars")

# Alt ve üst HSV değerleri için trackbar'lar oluşturuyoruz.
cv2.createTrackbar("Lower-H", "Trackbars", 90, 180, nothing)   # Alt Hue (renk tonu)
cv2.createTrackbar("Lower-S", "Trackbars", 50, 255, nothing)   # Alt Saturation (doygunluk)
cv2.createTrackbar("Lower-V", "Trackbars", 50, 255, nothing)   # Alt Value (parlaklık)
cv2.createTrackbar("Upper-H", "Trackbars", 130, 180, nothing)  # Üst Hue
cv2.createTrackbar("Upper-S", "Trackbars", 255, 255, nothing)  # Üst Saturation
cv2.createTrackbar("Upper-V", "Trackbars", 255, 255, nothing)  # Üst Value

while True:
    # Kameradan bir kare okuyoruz.
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü aynalıyoruz (sağ-sol ters çevriliyor)
    frame = cv2.flip(frame, 1)

    # BGR formatındaki görüntüyü HSV formatına çeviriyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan alınan değerleri kullanarak HSV renk aralıklarını ayarlıyoruz.
    lh = cv2.getTrackbarPos("Lower-H", "Trackbars")
    ls = cv2.getTrackbarPos("Lower-S", "Trackbars")
    lv = cv2.getTrackbarPos("Lower-V", "Trackbars")
    uh = cv2.getTrackbarPos("Upper-H", "Trackbars")
    us = cv2.getTrackbarPos("Upper-S", "Trackbars")
    uv = cv2.getTrackbarPos("Upper-V", "Trackbars")

    # HSV renk eşikleme aralığını belirliyoruz.
    lower_blue = np.array([lh, ls, lv])  # Alt renk eşiği
    upper_blue = np.array([uh, us, uv])  # Üst renk eşiği

    # Maskeyi oluşturuyoruz (Sadece belirlenen renkleri içeren bir görüntü oluşturur).
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskeyi kullanarak sadece belirlenen rengi içeren bir görüntü oluşturuyoruz.
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri ekranda gösteriyoruz.
    cv2.imshow("Original Frame", frame)  # Orijinal kamera görüntüsü
    cv2.imshow("Mask", mask)  # Siyah-beyaz maskelenmiş görüntü
    cv2.imshow("Filtered Result", result)  # Sadece mavi olan bölümleri gösteren görüntü

    # 'q' tuşuna basıldığında döngüyü kır ve programı kapat.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatıyoruz.
cap.release()
cv2.destroyAllWindows()
