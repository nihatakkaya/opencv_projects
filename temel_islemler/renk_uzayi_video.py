import cv2  # OpenCV kütüphanesini içe aktarır

# "webcam.avi" adlı video dosyasını açar
cap = cv2.VideoCapture("webcam.avi")

# Video oynatma döngüsü başlar
while True:
    # Videodan bir kare okur
    ret, frame = cap.read()
    
    # Eğer kare okunamazsa (video biterse), döngüyü kır
    if ret == False:
        break
    
    # Kareyi gri tonlamaya çevirir
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Gri tonlamalı kareyi ekranda gösterir
    cv2.imshow("Video", frame)
    
    # Kullanıcı "q" tuşuna basarsa döngüden çıkar
    if cv2.waitKey(30) & 0XFF == ord("q"):
        break

# Video dosyasını serbest bırakır
cap.release()

# Açılan tüm OpenCV pencerelerini kapatır
cv2.destroyAllWindows()
