import cv2
import numpy as np

# Görüntüyü yükleme
image_path = "para.jpg"  # Yüklenen dosyanın yolu
img = cv2.imread(image_path)

# Görüntüyü gri tonlamaya çevirme
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için Gaussian Blur uygulama
blur = cv2.GaussianBlur(gray, (15, 15), 0)

# Kenarları belirlemek için Canny Edge Detection kullanma
edges = cv2.Canny(blur, 50, 150)

# Daireleri tespit etmek için Hough Transform kullanma
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=30, minRadius=20, maxRadius=60)

# Eğer daireler bulunduysa
if circles is not None:
    circles = np.uint16(np.around(circles))  # Daire koordinatlarını tamsayıya çevir

    # Tespit edilen her para için çember çiz
    for circle in circles[0, :]:
        x, y, r = circle
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)  # Yeşil daire
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)  # Merkez noktayı kırmızı göster

    # Sol üst köşeye toplam para sayısını yazdır
    cv2.putText(img, f"para adedi: {len(circles[0])}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

# Sonucu gösterme
cv2.imshow("para bulma", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
