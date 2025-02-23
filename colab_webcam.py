import cv2
from ultralytics import YOLO


model = YOLO('C:/Users/Lenovo/Desktop/col_ik/runs/detect/train2/weights/best.pt')


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    
    results = model(frame)

    
    annotated_frame = results[0].plot()  

    
    cv2.imshow('YOLOv8 - UAV Detection', annotated_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

"""

import cv2
import numpy as np
from ultralytics import YOLO
import mediapipe as mp

# YOLO modelini yükle
model = YOLO('C:/Users/Lenovo/Desktop/col_ik/runs/detect/train2/weights/best.pt')

# Webcam başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break


    results = model(frame, conf=0.5, iou=0.45)  

    for detection in results[0].boxes.data.tolist():  
        x1, y1, x2, y2, conf, cls = detection

        width, height = x2 - x1, y2 - y1

       
        if width < 50 or height < 50:  
            continue

       
        roi = frame[int(y1):int(y2), int(x1):int(x2)]  
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  
        mean_intensity = np.mean(gray_roi)  

        if mean_intensity > 180:  
            continue

        
        aspect_ratio = width / height  
        if aspect_ratio < 0.3 or aspect_ratio > 3.5:  # Daha geniş bir aralık belirledik
            continue
        
        # 4️⃣ **Güven Skoru Yüksekse Çiz**
        if conf > 0.5:  # Daha fazla tespit için eşik değerini düşürdük
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"SIHA {conf:.2f}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Güncellenmiş görüntüyü göster
    cv2.imshow('YOLOv8 - UAV Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""