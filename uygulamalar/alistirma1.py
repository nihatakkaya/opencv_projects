import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# Kamerayı başlatır
cap = cv2.VideoCapture(0)  # 0, varsayılan web kamerayı temsil eder

# Belirli bir rengi HSV formatında tanımla (Örneğin: Siyah Renk)
lower_bound = np.array([0, 0, 0])  # Alt HSV sınırı (siyah için)
upper_bound = np.array([180, 255, 50])  # Üst HSV sınırı (siyah için)

while True:
    ret, frame = cap.read()  # Kameradan bir kare okur
    frame = cv2.flip(frame, 1)  # Aynada gördüğümüz gibi görüntüyü yatay çevirir

    # Görüntüyü HSV formatına çevirir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirtilen renk aralığında kalan pikselleri beyaz (255), diğerlerini siyah (0) yapan bir maske oluşturur
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Maske ile orijinal görüntüyü AND işlemine sokarak yalnızca belirlenen renkli bölgeleri gösterir
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal görüntüyü ekranda gösterir
    cv2.imshow("Original", frame)

    # Maske görüntüsünü ekranda gösterir
    cv2.imshow("Mask", mask)

    # Yalnızca tespit edilen rengi içeren sonucu gösterir
    cv2.imshow("Detected Color", result)

    # Kullanıcı 'q' tuşuna basarsa döngüyü kır ve çık
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırakır
cap.release()

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
