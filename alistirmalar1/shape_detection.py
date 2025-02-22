import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# OpenCV'nin içinde bulunan yazı tiplerini belirliyoruz.
font = cv2.FONT_HERSHEY_SIMPLEX  # Basit bir yazı tipi.
font1 = cv2.FONT_HERSHEY_COMPLEX  # Daha kompleks bir yazı tipi.

# Görüntüyü okuyoruz.
img = cv2.imread("1.1 polygons.png.png")

# Görüntüyü gri tonlamaya çeviriyoruz.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüye eşikleme (thresholding) uygulayarak ikili (binary) hale getiriyoruz.
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Görüntüdeki şekillerin dış hatlarını (contours) buluyoruz.
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Tespit edilen her konturu döngüyle işliyoruz.
for cnt in contours:

    # Konturun çevresini hesaplıyoruz ve buna bağlı olarak yaklaşık bir şekil belirliyoruz.
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Bulunan şeklin konturunu çiziyoruz.
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)  # Siyah renk (0,0,0) ve 3 piksel kalınlık ile çiziyoruz.

    # Şeklin etrafına dikdörtgen çizerek koordinatlarını alıyoruz.
    x, y, w, h = cv2.boundingRect(approx)

    # Yazıyı şeklin ortasına daha yakın koymak için X ve Y hesaplıyoruz.
    text_x = x + w // 4  # Metni şeklin merkezine daha yakın koyuyoruz.
    text_y = y + h // 2

    # Şeklin kaç kenarı olduğunu kontrol ederek adını belirtiyoruz.
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (text_x, text_y), font1, 1, (0, 0, 255), 2)  # Kırmızı Üçgen yazısı

    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (text_x, text_y), font1, 1, (0, 255, 0), 2)  # Yeşil Dörtgen yazısı

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (text_x, text_y), font1, 1, (255, 0, 0), 2)  # Mavi Beşgen yazısı

    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (text_x, text_y), font1, 1, (255, 255, 0), 2)  # Sarı Altıgen yazısı

    else:
        cv2.putText(img, "Ellipse", (text_x, text_y), font1, 1, (0, 255, 255), 2)  # Camgöbeği Elips yazısı

# İşlenmiş görüntüyü ekranda gösteriyoruz.
cv2.imshow("IMG", img)

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
