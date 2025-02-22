import cv2  # OpenCV kütüphanesini içe aktarıyoruz.

# Video dosyasını açıyoruz.
cap = cv2.VideoCapture("5.1 car.mp4.mp4")

# Çizilecek dairelerin merkez noktalarını saklamak için bir liste oluşturuyoruz.
circles = []

# Mouse olaylarını takip eden fonksiyon tanımlıyoruz.
def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:  # Eğer sol fare tuşuna basılırsa
        circles.append((x, y))  # Fare tıklanan noktayı 'circles' listesine ekliyoruz.

# "Frame" adlı bir pencere oluşturuyoruz.
cv2.namedWindow("Frame")

# Pencereye mouse callback fonksiyonunu bağlıyoruz.
cv2.setMouseCallback("Frame", mouse)

# Sonsuz döngü ile videoyu kare kare okuyoruz.
while True:
    _, frame = cap.read()  # Videodan bir kare okuyoruz.

    # Eğer video biterse döngüyü kır.
    if frame is None:
        break

    # Okunan kareyi 640x480 boyutuna yeniden boyutlandırıyoruz.
    frame = cv2.resize(frame, (640, 480))

    # 'circles' listesinde kayıtlı olan her noktaya bir daire çiziyoruz.
    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), -1)  # Mavi renkte (255,0,0), 20 piksel çapında dolu daire çiziyoruz.

    # Güncellenmiş kareyi ekranda gösteriyoruz.
    cv2.imshow("Frame", frame)

    # Klavyeden bir tuşa basılmasını bekliyoruz.
    key = cv2.waitKey(1)

    if key == 27:  # ESC (27) tuşuna basılırsa döngüden çık.
        break
    elif key == ord("h"):  # 'h' tuşuna basıldığında tüm noktaları temizle.
        circles = []

# Video dosyasını serbest bırakıyoruz.
cap.release()

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
