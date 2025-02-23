import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # NumPy kütüphanesini içe aktarıyoruz.

# Kullanılacak görüntülerin dosya yollarını tanımlıyoruz.
image_path = "5.1 starwars.jpg.jpg"  # Ana görüntünün yolu
template_path = "5.2 starwars2.jpg.jpg"  # Aranacak şablon (template) görüntüsünün yolu

# Ana görüntüyü okuyoruz.
img = cv2.imread(image_path)  # Belirtilen ana görüntüyü okuyoruz.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Ana görüntüyü gri tonlamaya çeviriyoruz.

# Şablon (template) görüntüyü okuyoruz ve gri tonlamada alıyoruz.
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)  # Şablon görüntüsünü gri tonlamada okuyoruz.
w, h = template.shape[::-1]  # Şablonun genişlik (w) ve yükseklik (h) değerlerini alıyoruz.

# Şablon eşleşmesi (template matching) işlemini gerçekleştiriyoruz.
result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# Şablonun ana görüntüdeki en iyi eşleşen konumlarını belirliyoruz.
location = np.where(result >= 0.95)
# Eşik değeri 0.95 olarak belirlenmiştir, yani yalnızca %95 veya daha fazla eşleşen bölgeler işaretlenecektir.

# Bulunan eşleşmeleri dikdörtgenlerle işaretliyoruz.
for point in zip(*location[::-1]):  # Eşleşen noktaları döngü ile işliyoruz.
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (0, 255, 0), 3)
    # Eşleşen bölgenin üzerine yeşil (0, 255, 0) renkli bir dikdörtgen çiziyoruz.

# Sonuç görüntüsünü ekranda gösteriyoruz.
cv2.imshow("Image", img)  # İşaretlenmiş görüntüyü ekranda gösteriyoruz.

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)  # Kullanıcı bir tuşa basana kadar pencereyi açık tutuyoruz.

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
