import cv2  # OpenCV kütüphanesini içe aktarıyoruz
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz

# 1. Resmi yükleme
img = cv2.imread(r"para3.jpg")  # "para3.jpg" dosyasını okuyup img değişkenine atıyoruz

# 2. Resmi gri tonlamaya çevirme
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR formatındaki resmi gri formata dönüştürüyoruz

# 3. Histogram eşitleme ile kontrastı artırma
gray = cv2.equalizeHist(gray)  # Farklı parlaklık seviyelerine sahip resmi daha dengeli hale getirir

# 4. Median Blur uygulama (gürültüyü azaltma)
img_blur = cv2.medianBlur(gray, 7)  # 7x7 boyutlu bir çekirdek ile medyan bulanıklaştırma

# 5. Hough Circle Transform ile daire tespiti
circles = cv2.HoughCircles(
    img_blur,              # Bulanıklaştırılmış gri resim
    cv2.HOUGH_GRADIENT,    # Hough dönüşümü yöntemi (gradient bazlı)
    4.3,                   # dp: Çözünürlük ölçekleme parametresi (daha yüksek değer -> daha düşük çözünürlük)
    img.shape[0] / 6,      # minDist: Daire merkezleri arasındaki minimum mesafe
    param1=300,            # Canny kenar algılama için üst eşik değeri
    param2=500,            # Daire tespiti için birikim matrisi eşik değeri (daha yüksek -> daha az ama daha güvenilir tespit)
    minRadius=100,         # Tespit edilecek dairenin minimum yarıçapı
    maxRadius=270          # Tespit edilecek dairenin maksimum yarıçapı
)

# 6. Eğer daireler bulunduysa...
if circles is not None:
    # ...float değerleri tamsayıya yuvarlıyoruz
    circles = np.uint16(np.around(circles))

    # Bir sayaç tanımlayarak daire sayısını tutacağız
    count = 0
    # Tespit edilen her daire için döngüye giriyoruz
    for i in circles[0, :]:
        count += 1  # Her daire bulunduğunda sayacı 1 artırıyoruz
        # Dairenin merkezini (i[0], i[1]) ve yarıçapını i[2] kullanarak çiziyoruz
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Yeşil renkli (0,255,0) ve 2 piksel kalınlık

    # Daire sayısını resmin sol üst köşesine yazdırıyoruz
    cv2.putText(img, f"para sayisi: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2, cv2.LINE_AA)

# 7. Resmi ekranda gösterme (600x480'e yeniden boyutlandırıyoruz)
img = cv2.resize(img, (600, 480))  # Görüntünün ekranda daha küçük gösterilmesi için yeniden boyutlandırma
cv2.imshow("img", img)             # "img" başlıklı bir pencere açarak resmi gösteriyoruz

# 8. Bir tuşa basılana kadar bekliyoruz, ardından pencereyi kapatıyoruz
cv2.waitKey(0)
cv2.destroyAllWindows()
