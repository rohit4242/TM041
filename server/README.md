# Cow Detection System

This repository contains a Python script for detecting cows in a video stream using the YOLO (You Only Look Once) object detection algorithm. Detected cows are then displayed in real-time on the video stream and logged to a Firebase database.

## Table of Contents

- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Dependencies

- Python 3.x
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) - YOLOv5 object detection model
- OpenCV (`cv2`)
- Pyrebase
- Pyrebase
- Plyer
- Dotenv

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/rohit4242/cow-detection-system.git
    cd server
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. Ensure your webcam is connected or provide the path to your video file.
2. Run the Python script:

    ```bash
    python cattle_detection_with_single_video.py or
    python cattle_detection_with_multiple_video.py

    ```

3. The script will start processing the video stream, detecting cows, and displaying them in real-time. Detected cows will also be logged to the Firebase database.

4. Press `q` to quit the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
