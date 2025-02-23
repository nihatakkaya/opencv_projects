import cv2  # OpenCV kütüphanesini içe aktarıyoruz.

# Görüntüyü okuyoruz.
img = cv2.imread("4.2 starwars.jpg.jpg")  # Belirtilen yolu kullanarak görüntüyü okuyoruz.

# Görüntüyü bulanıklaştırıyoruz (Median Blur uyguluyoruz).
blurry_img = cv2.medianBlur(img, 9)  # 9x9 kernel ile medyan bulanıklaştırma (gürültü azaltma) işlemi yapıyoruz.

# Laplacian yöntemi ile görüntünün keskinliğini (sharpness) ölçüyoruz.
laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
# Laplacian dönüşümü ile görüntünün ikinci türevini alıyoruz ve varyansını (keskinlik ölçütü) hesaplıyoruz.

print(laplacian)  # Laplacian varyans değerini ekrana yazdırıyoruz.

# Eğer Laplacian değeri 500'den küçükse görüntüyü bulanık olarak değerlendiriyoruz.
if laplacian < 500:
    print("blurry image")  # Konsola "blurry image" mesajını yazdırıyoruz.

# Orijinal ve bulanık görüntüyü ekranda gösteriyoruz.
cv2.imshow("img", img)  # "img" başlığıyla orijinal görüntüyü gösteriyoruz.
cv2.imshow("blurry_img", blurry_img)  # "blurry_img" başlığıyla bulanık görüntüyü gösteriyoruz.

# Kullanıcının bir tuşa basmasını bekliyoruz.
cv2.waitKey(0)  # Kullanıcı bir tuşa basana kadar pencereyi açık tutar.

# Açık olan tüm OpenCV pencerelerini kapatıyoruz.
cv2.destroyAllWindows()
