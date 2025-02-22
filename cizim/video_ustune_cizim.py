import cv2
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

file_name = "C:\\Users\\Nihat\\OneDrive\\Masaüstü\\ARTEK\\webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frame_rate = 30
resolution = (640, 480)
video_output = cv2.VideoWriter(file_name, codec, frame_rate, resolution)

frame_count = 0
save_dir = "C:\\Users\\Nihat\\OneDrive\\Masaüstü\\ARTEK\\captured_frames"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera akışı alınamıyor!")
        break

    frame = cv2.flip(frame, 1)

    top_left = (100,100)
    bottom_right = (300,300)
    renk = (0, 255, 0) #yeşil renk
    kalinlik = 2
    cv2.rectangle(frame, top_left, bottom_right, renk, kalinlik)

    video_output.write(frame)

    cv2.imshow("Webcam Live", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('n'):
        img_path = os.path.join(save_dir, f"frame_{frame_count}.png")
        cv2.imwrite(img_path, frame)
        print(f"Kare kaydedildi: {img_path}")
        frame_count += 1

    elif key == ord('l'):
        print("Uygulama kapatılıyor...")
        break

video_output.release()
cap.release()
cv2.destroyAllWindows()
