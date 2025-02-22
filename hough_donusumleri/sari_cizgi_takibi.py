import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Video dosyasını açmak için VideoCapture kullanıyoruz.
# Dosya adı yanlış olabilir veya dosya tamamlanmamış olabilir (".crdownload" uzantısı indirme tamamlanmadığını gösterir).
vid = cv2.VideoCapture("4.2 line.mp4.mp4.crdownload")

# Sonsuz döngü ile videodaki her kareyi okuyoruz.
while True:
    ret, frame = vid.read()  # Videodan bir kare okuyoruz.

    # Eğer video bitti veya kare okunamadıysa döngüyü kırıyoruz.
    if not ret:
        break

    # Görüntüyü 640x480 boyutuna yeniden boyutlandırıyoruz.
    frame = cv2.resize(frame, (640, 480))

    # BGR formatındaki görüntüyü HSV renk uzayına çeviriyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # HSV renk uzayı kullanılarak renk tespiti yapılacak.

    # Sarı rengin alt ve üst sınırlarını belirliyoruz (HSV formatında).
    lower_yellow = np.array([18, 94, 140], np.uint8)  # Minimum sarı renk tonu
    upper_yellow = np.array([48, 255, 255], np.uint8)  # Maksimum sarı renk tonu

    # HSV görüntüsü üzerinde belirlenen renk aralığında maskeleme yapıyoruz.
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Maskelenmiş görüntüde kenarları belirlemek için Canny kenar algılama kullanıyoruz.
    edges = cv2.Canny(mask, 75, 250)

    # Hough Line Transform kullanarak tespit edilen kenarların doğrularını belirliyoruz.
    # Parametreler:
    # - 1: Rho çözünürlüğü (piksel cinsinden).
    # - np.pi / 180: Açı çözünürlüğü (radyan cinsinden).
    # - 50: Bir doğruyu oluşturmak için gereken minimum oylama sayısı.
    # - maxLineGap=50: Bir doğruyu oluşturan maksimum kesinti uzunluğu.
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)

    # Eğer tespit edilen çizgiler varsa bunları çiziyoruz.
    if lines is not None:
        for line in lines:
            (x1, y1, x2, y2) = line[0]  # Çizginin başlangıç ve bitiş koordinatlarını alıyoruz.
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0),
                     5)  # Yeşil renkte (0,255,0) ve 5 piksel kalınlığında çiziyoruz.

    # İşlenen görüntüyü ekranda gösteriyoruz.
    cv2.imshow("IMG", frame)

    # Klavyeden 'q' tuşuna basıldığında döngüyü kır ve çık.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Videoyu serbest bırakıyoruz ve pencereleri kapatıyoruz.
vid.release()
cv2.destroyAllWindows()
