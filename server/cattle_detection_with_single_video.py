from ultralytics import YOLO
import cv2
import math
from datetime import datetime
import os
from dotenv import load_dotenv
import pyrebase
from plyer import notification

load_dotenv()

config = {
    "apiKey": "AIzaSyD2sqM7OQ5f6YOuydS3JKuMvrQtYBTrQP8",
    "authDomain": "hackathon-cattle-detectio-2024.firebaseapp.com",
    "databaseURL": "https://hackathon-cattle-detectio-2024-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "hackathon-cattle-detectio-2024.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


def update_firebase_batch(updates):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    batch_data = {}

    for index, data in updates.items():
        status = data['status']
        cow_detection = status == 'cow'  # True if status is 'cow', False otherwise
        update_time = now
        batch_data[f"cow_{index}"] = {"status": status, "cow_detection": cow_detection, "update_time": update_time}

    db.update(batch_data)



# start webcam
cap = cv2.VideoCapture('dataset/sample_videos/4.mp4')
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("dataset/model.pt")
# object classes
classNames = ["2", "3"]

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    spaceCounter = 0
    update_batch = {}  # Collect updates in a batch

    # coordinates
    for r in results:
        boxes = r.boxes

        for index, box in enumerate(boxes, start=1):
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            # confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            label = classNames[cls]
            print("Class name -->", label)
            status = "not detection"  # Default status
            if label == "2":
                notification.notify(
                    title=f"Cow-{label}",
                    message="Cow is Detecting",
                    app_icon=None,
                    timeout=10,
                )

                status = "cow"
                spaceCounter += 1
            else: 
                status = "not detection"
                spaceCounter += 1
            update_batch[index] = {"status": status}

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            thickness = 1
            color = (255, 0, 0)

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    update_firebase_batch(update_batch)  # Send batched updates

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()