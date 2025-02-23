import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Karşılaştırılacak iki görüntünün dosya yollarını tanımlıyoruz.
path1 = r"C:\Users\Nihat\Downloads\.1 aircraft.jpg.jpg"  # Birinci görüntü yolu
path2 = r"C:\Users\Nihat\Downloads\1.1 aircraft.jpg.jpg"  # İkinci görüntü yolu

# İlk görüntüyü okuyoruz.
img1 = cv2.imread(path1)
if img1 is None:
    print("Error: First image not found or invalid path!")
    exit()

img1 = cv2.resize(img1, (640, 550))  # Görüntüyü 640x550 boyutuna yeniden boyutlandırıyoruz.

# İkinci görüntüyü okuyoruz.
img2 = cv2.imread(path2)
if img2 is None:
    print("Error: Second image not found or invalid path!")
    exit()

img2 = cv2.resize(img2, (640, 550))  # Görüntüyü 640x550 boyutuna yeniden boyutlandırıyoruz.

# İki görüntü arasındaki farkı hesaplıyoruz.
diff = cv2.subtract(img1, img2)  # Doğru karşılaştırma: img1 - img2

# Eğer fark hesaplanamadıysa hata mesajı ver.
if diff is None:
    print("Error: Difference image could not be computed!")
    exit()

# Fark görüntüsünü RGB kanallarına ayırıyoruz.
b, g, r = cv2.split(diff)

# Görüntüler tamamen eşit mi kontrol ediyoruz.
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("completely equal")  # Eğer fark yoksa görüntüler tamamen eşittir.
else:
    print("NOT completely equal")  # Eğer fark varsa görüntüler eşit değildir.

# Fark görüntüsünü ekranda gösteriyoruz.
cv2.imshow("Difference", diff)  # "Difference" başlığıyla fark görüntüsünü ekrana getiriyoruz.

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)  # Kullanıcı bir tuşa basana kadar pencereyi açık tutar.

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
