import cv2  # OpenCV kütüphanesini içe aktarır

# "klonasker.jpg" adlı resmi okur ve img değişkenine atar
img = cv2.imread("klonasker.jpg")

# Görüntüyü farklı renk uzaylarına dönüştürür
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye çevirir
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR'den HSV'ye çevirir
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR'den Gri tonlamaya çevirir

# Görüntüleri yeni bir boyuta (1000x720 piksel) yeniden boyutlandırır
img = cv2.resize(img, (1000,720))
img_rgb = cv2.resize(img_rgb, (1000,720))
img_hsv = cv2.resize(img_hsv, (1000,720))
img_gray = cv2.resize(img_gray, (1000,720))

# Görüntüleri ekranda gösterir
cv2.imshow("Klonasker BGR", img)
cv2.imshow("Klonasker RGB", img_rgb)
cv2.imshow("Klonasker HSV", img_hsv)
cv2.imshow("Klonasker GRAY", img_gray)

# Kullanıcıdan bir tuşa basmasını bekler ve ardından devam eder
cv2.waitKey(0)

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()