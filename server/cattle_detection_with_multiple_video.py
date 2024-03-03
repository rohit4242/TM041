from ultralytics import YOLO
import cv2
import math
from datetime import datetime
import os
from dotenv import load_dotenv
import pyrebase
import threading
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


# Function to process frames from video 1
def process_video1():
    cap1 = cv2.VideoCapture('dataset/sample_videos/5.mp4')
    model1 = YOLO("dataset/model.pt")
    classNames1 = ["2", "3"]
    while True:
        success1, img1 = cap1.read()
        if not success1:
            break
        results1 = model1(img1, stream=True)

        spaceCounter = 0
        update_batch = {}  # Collect updates in a batch

        # coordinates
        for r1 in results1:
            boxes1 = r1.boxes

            for index1, box1 in enumerate(boxes1, start=1):
                # bounding box
                x1, y1, x2, y2 = box1.xyxy[0]
                x1, y1, x2, y2 = (
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2),
                )  # convert to int values

                # put box in cam
                cv2.rectangle(img1, (x1, y1), (x2, y2), (255, 0, 255), 2)

                # confidence
                confidence = math.ceil((box1.conf[0] * 100)) / 100
                print("Confidence --->", confidence)

                # class name
                cls = int(box1.cls[0])
                label = classNames1[cls]
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
                update_batch[index1] = {"status": status}

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                thickness = 1
                color = (255, 0, 0)

                cv2.putText(
                    img1, classNames1[cls], org, font, fontScale, color, thickness
                )

        update_firebase_batch(update_batch)  # Send batched updates

        cv2.imshow("Webcam1", img1)
        if cv2.waitKey(1) == ord("q"):
            break

    cap1.release()
    cv2.destroyAllWindows()


# Function to process frames from video 2
def process_video2():
    cap2 = cv2.VideoCapture('dataset/sample_videos/6.mp4')
    model2 = YOLO("dataset/model.pt")
    classNames2 = ["2", "3"]
    while True:
        success2, img2 = cap2.read()
        if not success2:
            break
        results2 = model2(img2, stream=True)

        spaceCounter = 0
        update_batch = {}  # Collect updates in a batch

        # coordinates
        for r2 in results2:
            boxes2 = r2.boxes

            for index2, box2 in enumerate(boxes2, start=1):
                # bounding box
                x1, y1, x2, y2 = box2.xyxy[0]
                x1, y1, x2, y2 = (
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2),
                )  # convert to int values

                # put box in cam
                cv2.rectangle(img2, (x1, y1), (x2, y2), (255, 0, 255), 2)

                # confidence
                confidence = math.ceil((box2.conf[0] * 100)) / 100
                print("Confidence --->", confidence)

                # class name
                cls = int(box2.cls[0])
                label = classNames2[cls]
                print("Class name -->", label)
                status = "not detection"  # Default status
                if label == "2":
                    print("Yes")  # Print "Yes" when object "2" is detected
                    status = "cow"
                    spaceCounter += 1

                update_batch[index2] = {"status": status}

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                thickness = 1
                color = (255, 0, 0)

                cv2.putText(
                    img2, classNames2[cls], org, font, fontScale, color, thickness
                )

        update_firebase_batch(update_batch)  # Send batched updates

        cv2.imshow("Webcam2", img2)
        if cv2.waitKey(1) == ord("q"):
            break

    cap2.release()
    cv2.destroyAllWindows()


# Create threads for processing frames from each video
thread1 = threading.Thread(target=process_video1)
thread2 = threading.Thread(target=process_video2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()