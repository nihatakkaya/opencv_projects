import cv2
import os

#kamera için gereklii şeyler
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #kamerayı açar. 0 ilk kamerayı ifade eder, cv2.cap_dshow da windows işletim sisteminde bazı kamera sorunlarını önlemek için kullandığımız bir parametre

# Video kaydı için gerekli şeyler
file_name = "C:\\Users\\Nihat\\OneDrive\\Masaüstü\\ARTEK\\webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frame_rate = 30 #videonun saniyede kaç kere yakalanacağını belirtir yani fps
resolution = (640, 480) #videonun çözünürlüğü
video_output = cv2.VideoWriter(file_name, codec, frame_rate, resolution)    #video dosyasına kareleri kaydetmek için


frame_count = 0
save_dir = "C:\\Users\\Nihat\\OneDrive\\Masaüstü\\ARTEK\\captured_frames" # kaydedilecek dosyanın adresi

# Eğer kayıt dosyası yoksa yeni kayıt dosyası oluşturup hata almamak için
if not os.path.exists(save_dir):    #belirtilen klasörün var olup olmadığını kontrol eder
    os.makedirs(save_dir)       #klasör yoksa oluştur

while True:
    ret, frame = cap.read() # kameradan kare alır
    if not ret:
        print("Kamera akışı alınamıyor!")
        break

    frame = cv2.flip(frame, 1)  # kameradaki görüntüyü ayna olarak yansıtır gösterir
    video_output.write(frame)  # videoyu kaydeder

    cv2.imshow("Webcam Live", frame) #anlık görüntüyü pencere içinde göstermek için

    key = cv2.waitKey(1) & 0xFF #klavyeden girdi almak için

    if key == ord('n'):  # n tuşuna basıldığında o anki kareyi kaydeder
        img_path = os.path.join(save_dir, f"frame_{frame_count}.png") #kaydedilecek görüntünün dosya yolunu oluşturur
        cv2.imwrite(img_path, frame) #görüntüyü png olarak kaydeder.
        print(f"Kare kaydedildi: {img_path}")
        frame_count += 1 #bir sonraki kaydedilecek görüntünün numarasını arttırır

    elif key == ord('l'):  #l tuşuna basıldığında çıkması için
        print("Uygulama kapatılıyor...")
        break


video_output.release()  #videoyu kaydetme işlemini bitirir ve dosyayı kapatır
cap.release() #kamerayı serbest bırakır
cv2.destroyAllWindows() #açılan tüm opencv dosyalarını kapatır
