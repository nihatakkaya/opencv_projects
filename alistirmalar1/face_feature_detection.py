import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.
import math  # Matematiksel işlemler için math kütüphanesini içe aktarıyoruz.


# En büyük konturu bulan fonksiyon
def findMaxContour(contours):
    max_i = 0  # En büyük alanın indeksini tutacak değişken.
    max_area = 0  # En büyük alanı tutacak değişken.

    for i in range(len(contours)):  # Tüm konturlar arasında dolaşıyoruz.
        area_face = cv2.contourArea(contours[i])  # Konturun alanını hesaplıyoruz.

        if max_area < area_face:  # Eğer yeni alan daha büyükse, onu kaydediyoruz.
            max_area = area_face
            max_i = i  # Yeni maksimum alanın indeksini güncelliyoruz.

    try:
        c = contours[max_i]  # En büyük konturu seçiyoruz.
    except:
        contours = [0]  # Eğer kontur bulunamazsa, varsayılan bir değer atıyoruz.
        c = contours[0]

    return c  # En büyük konturu döndürüyoruz.


# Kamerayı başlatıyoruz.
cap = cv2.VideoCapture(0)  # Bilgisayarın varsayılan kamerasını açıyoruz.

# Sonsuz döngü içinde kameradan görüntü almaya başlıyoruz.
while True:
    ret, frame = cap.read()  # Kameradan bir kare okuyoruz.

    if not ret:  # Eğer görüntü alınamazsa, döngüyü kır.
        break

    frame = cv2.flip(frame, 1)  # Aynalama işlemi yaparak görüntüyü soldan sağa çeviriyoruz.

    # ROI (Region of Interest) belirliyoruz. Çerçevenin içindeki bir dikdörtgen alanı alıyoruz.
    roi = frame[50:250, 200:400]  # frame[y1:y2, x1:x2]

    # ROI alanını kırmızı bir dikdörtgenle çerçeveliyoruz.
    cv2.rectangle(frame, (200, 50), (400, 250), (0, 0, 255), 0)

    # ROI alanını HSV renk uzayına çeviriyoruz.
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Renk eşikleme aralığını belirliyoruz.
    lower_color = np.array([0, 45, 79], dtype=np.uint8)  # Alt HSV değeri
    upper_color = np.array([17, 255, 255], dtype=np.uint8)  # Üst HSV değeri

    # Belirlenen HSV aralığında maskelenmiş görüntü oluşturuyoruz.
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Gürültüleri azaltmak için görüntü işleme adımları:
    kernel = np.ones((3, 3), np.uint8)  # 3x3 boyutunda bir kernel (çekirdek) oluşturuyoruz.
    mask = cv2.dilate(mask, kernel, iterations=1)  # Dilation işlemi uygulayarak maskeyi genişletiyoruz.
    mask = cv2.medianBlur(mask, 15)  # Median blur ile maskeyi daha düzgün hale getiriyoruz.

    # Konturları (nesne sınırlarını) buluyoruz.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:  # Eğer en az bir kontur bulunursa
        c = findMaxContour(contours)  # En büyük konturu buluyoruz.

        # Konturun en uç noktalarını buluyoruz.
        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # En sol nokta
        extRight = tuple(c[c[:, :, 0].argmax()][0])  # En sağ nokta
        extTop = tuple(c[c[:, :, 1].argmin()][0])  # En üst nokta
        extBot = tuple(c[c[:, :, 1].argmax()][0])  # En alt nokta

        # En uç noktaları işaretlemek için daireler çiziyoruz.
        cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)  # Sol uç nokta
        cv2.circle(roi, extRight, 5, (0, 255, 0), 2)  # Sağ uç nokta
        cv2.circle(roi, extTop, 5, (0, 255, 0), 2)  # Üst uç nokta
        cv2.circle(roi, extBot, 5, (0, 255, 0), 2)  # Alt uç nokta

        # Dış noktaları birleştirerek şeklin sınırlarını belirginleştiriyoruz.
        cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)
        cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
        cv2.line(roi, extRight, extBot, (255, 0, 0), 2)
        cv2.line(roi, extBot, extLeft, (255, 0, 0), 2)

        # Üçgenin kenar uzunluklarını hesaplıyoruz.
        a = math.sqrt((extRight[0] - extTop[0]) ** 2 + (extRight[1] - extTop[1]) ** 2)  # Sağ-Üst
        b = math.sqrt((extBot[0] - extRight[0]) ** 2 + (extBot[1] - extRight[1]) ** 2)  # Sağ-Alt
        c = math.sqrt((extBot[0] - extTop[0]) ** 2 + (extBot[1] - extTop[1]) ** 2)  # Üst-Alt

        try:
            # Üçgenin açılarını hesaplıyoruz (Kosünüs Teoremi kullanarak).
            angle_ab = int(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * c)) * 57)  # Açıyı dereceye çeviriyoruz.

            # Hesaplanan açıyı ekrana yazdırıyoruz.
            cv2.putText(roi, str(angle_ab), (extRight[0] - 100 + 50, extRight[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        except:
            # Eğer hesaplama başarısız olursa "?" karakteri ekrana yazdırılır.
            cv2.putText(roi, " ? ", (extRight[0] - 100 + 50, extRight[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Kameradan alınan orijinal görüntüyü ekranda gösteriyoruz.
    cv2.imshow("frame", frame)

    # ROI (belirlenen bölge) görüntüsünü ekranda gösteriyoruz.
    cv2.imshow("roi", roi)

    # Maskeyi ekranda gösteriyoruz.
    cv2.imshow("mask", mask)

    # 'q' tuşuna basıldığında döngüden çıkıyoruz.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırakıyoruz.
cap.release()

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
