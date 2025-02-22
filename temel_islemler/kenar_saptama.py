# cv2.Canny(input, minThreshold, maxThreshold) → Canny algoritmasını kullanarak kenar tespiti yapar

import cv2  # OpenCV kütüphanesini içe aktarır

# Kamerayı başlatır
cap = cv2.VideoCapture(0)  # 0, varsayılan web kamerayı temsil eder

# Sürekli olarak kameradan görüntü alabilmek için sonsuz döngü başlatılır
while True:
    ret, frame = cap.read()  # Kameradan bir kare okur
    frame = cv2.flip(frame, 1)  # Aynada gördüğümüz gibi görüntüyü yatay çevirir

    # Canny kenar tespiti uygular
    # - frame: Kenar tespiti yapılacak görüntü
    # - 100: Minimum eşik değeri (minThreshold), düşük kenar eşiği
    # - 200: Maksimum eşik değeri (maxThreshold), yüksek kenar eşiği
    kenar = cv2.Canny(frame, 100, 200)

    # Orijinal görüntüyü ekranda gösterir
    cv2.imshow("Frame", frame)

    # Kenar tespiti yapılmış görüntüyü ekranda gösterir
    cv2.imshow("kenarlı", kenar)

    # Kullanıcı 'q' tuşuna basarsa döngüyü kır ve çık
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırakır
cap.release()

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()