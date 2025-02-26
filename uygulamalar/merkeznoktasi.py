import cv2

# Haar Cascade yüz algılama modelini yüklüyoruz
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlatıyoruz
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare okuyoruz
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü aynalıyoruz (sağ-sol ters çeviriyoruz)
    frame = cv2.flip(frame, 1)

    # Gri tonlamaya çeviriyoruz (Yüz tespiti için gereklidir)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit ediyoruz
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # Yüzün etrafına yeşil bir dikdörtgen çiziyoruz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Yüzün merkez noktasını hesaplıyoruz
        cx = x + w // 2  # X ekseninde merkez
        cy = y + h // 2  # Y ekseninde merkez

        # Yüzün merkez noktasını kırmızı bir daire ile gösteriyoruz
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Merkez noktasını ekrana yazdırıyoruz
        cv2.putText(frame, f"Center: ({cx}, {cy})", (cx - 50, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Görüntüyü ekranda gösteriyoruz
    cv2.imshow("Face Detection", frame)

    # 'q' tuşuna basıldığında döngüden çıkıyoruz
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatıyoruz
cap.release()
cv2.destroyAllWindows()
