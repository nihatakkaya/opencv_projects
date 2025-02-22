import cv2  # OpenCV kütüphanesini içe aktarır
import time  # Göz kapalı süresini takip etmek için zaman modülü

# OpenCV'nin hazır yüz ve göz tanıma modellerini yükler
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Kamerayı başlatır
cap = cv2.VideoCapture(0)

eye_closed_time = None  # Göz kapalı süresini takip eden değişken
EYE_CLOSED_THRESHOLD = 5  # Gözlerin kaç saniye kapalı kalması gerektiği (5 saniye)

while True:
    ret, frame = cap.read()  # Kameradan bir kare okur
    if not ret:
        break  # Eğer kare okunamazsa döngüden çık

    frame = cv2.flip(frame, 1)  # Ayna efekti uygular (görüntüyü yatay olarak çevirir)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevirir (yüz tespiti daha iyi çalışır)

    # Yüzleri tespit eder
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    eyes_detected = False  # Gözlerin açık olup olmadığını takip eder

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]  # Yüz bölgesini al
        roi_color = frame[y:y + h, x:x + w]

        # Gözleri tespit et
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))

        if len(eyes) > 0:
            eyes_detected = True  # En az bir göz bulunduğunda göz açık sayılır
            eye_closed_time = None  # Gözler açıldığı için zaman sıfırlanır

        # Eğer gözler kapalıysa süreyi başlat
        if not eyes_detected:
            if eye_closed_time is None:
                eye_closed_time = time.time()  # İlk göz kapandığında zamanı kaydet
            elif time.time() - eye_closed_time >= EYE_CLOSED_THRESHOLD:
                # Gözler belirlenen süre boyunca kapalı kaldıysa kırmızı dikdörtgen çiz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        else:
            # Gözler açık olduğu sürece yüzü yeşil kutu içine al
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Sonucu ekranda gösterir
    cv2.imshow("Face Tracking", frame)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
