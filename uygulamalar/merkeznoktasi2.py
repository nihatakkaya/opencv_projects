import cv2
import numpy as np

# Kamerayı başlatıyoruz
cap = cv2.VideoCapture(0)

# Mavi renk için HSV alt ve üst eşik değerlerini belirliyoruz
lower_blue = np.array([90, 50, 50])   # Alt HSV değeri (Mavi için)
upper_blue = np.array([130, 255, 255]) # Üst HSV değeri (Mavi için)

while True:
    # Kameradan bir kare okuyoruz
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü aynalıyoruz (sağ-sol ters çeviriyoruz)
    frame = cv2.flip(frame, 1)

    # BGR formatındaki görüntüyü HSV formatına çeviriyoruz
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi rengi tespit etmek için maskeyi oluşturuyoruz
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Gürültüyü azaltmak için morfolojik işlemler (Erosion ve Dilation)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Maskelenmiş görüntüde konturları (sınırları) buluyoruz
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Eğer en az bir kontur bulunursa
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)  # En büyük alanlı konturu seçiyoruz
        if cv2.contourArea(largest_contour) > 500:  # Küçük konturları görmezden geliyoruz.

            # En büyük konturun etrafına dikdörtgen çiziyoruz
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Yeşil dikdörtgen

            # Konturun merkez noktasını hesaplıyoruz
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])  # X eksenindeki merkezi hesapla
                cy = int(M["m01"] / M["m00"])  # Y eksenindeki merkezi hesapla

                # Merkezi kırmızı bir daire ile işaretliyoruz
                cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)  # Kırmızı daire (Merkez noktası)
                cv2.putText(frame, f"merkez: ({cx}, {cy})", (cx + 10, cy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Merkez koordinatlarını yazdır

    # Görüntüleri ekranda gösteriyoruz
    cv2.imshow("orijinal goruntu", frame)  # Orijinal kamera görüntüsü
    cv2.imshow("Maskeli", mask)  # Maskeleme işlemi yapılmış siyah-beyaz görüntü

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatıyoruz
cap.release()
cv2.destroyAllWindows()
