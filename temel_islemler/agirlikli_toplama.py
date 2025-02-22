# f(x,y) = x*a + y*b +c  --> İki görüntüyü ağırlıklı toplama işlemi formülü

import cv2  # OpenCV kütüphanesini içe aktarır
import numpy as np  # NumPy kütüphanesini içe aktarır

# Beyaz bir tuval (512x512 piksel, 3 kanal, uint8 veri tipi) oluşturur
circle = np.zeros((512,512,3), np.uint8) + 255

# Merkez noktası (256,256), yarıçapı 60 piksel olan mavi bir daire çizer
# -1 değeri, dairenin içini tamamen doldurmasını sağlar
cv2.circle(circle, (256,256), 60, (255,0,0), -1)

# Beyaz bir tuval (512x512 piksel, 3 kanal, uint8 veri tipi) oluşturur
rectangle = np.zeros((512,512,3), np.uint8) + 255

# Sol üst köşesi (150,150), sağ alt köşesi (350,350) olan kırmızı bir dikdörtgen çizer
# -1 değeri, dikdörtgenin içini tamamen doldurmasını sağlar
cv2.rectangle(rectangle, (150,150), (350, 350), (0, 0, 255), -1)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)

# İki görüntüyü ağırlıklı olarak birleştirir
# circle görüntüsüne %70 (0.7) ağırlık, rectangle görüntüsüne %30 (0.3) ağırlık verilir
# Sonuç olarak ortaya çıkan görüntü 'dst' değişkenine atanır
cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)

# Çizilen daireyi ekranda gösterir
cv2.imshow("Circle", circle)

# Çizilen dikdörtgeni ekranda gösterir
cv2.imshow("Rectangle", rectangle)

# Ağırlıklı toplam sonucu olan görüntüyü ekranda gösterir
cv2.imshow("Dst", dst)

# Kullanıcıdan bir tuşa basmasını bekler ve ardından devam eder
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()