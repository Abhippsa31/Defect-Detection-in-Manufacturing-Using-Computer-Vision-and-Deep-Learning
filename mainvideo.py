import cv2
from ultralytics import YOLO

model = YOLO('best_model.pt')  

# Open the webcam
cap = cv2.VideoCapture(0)  

cap.set(3, 640)  
cap.set(4, 480)  

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Perform inference
    results = model(frame)

    annotated_frame = results[0].plot()  # Draw bounding boxes and labels

    cv2.imshow('Real-time Defect Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
