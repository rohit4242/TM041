# Cow Detection System

This repository contains the code for a Cow Detection System. It consists of two main components: the client and the server.

## Table of Contents

- [Client](#client)
- [Server](#server)
- [License](#license)

## Client

The client folder contains the frontend code for the Cow Detection System. It is responsible for interacting with users, displaying the video stream, and providing a user interface for configuring and viewing detections.

### Dependencies

- HTML
- CSS
- JavaScript
- TypeScript
- Frontend framework (e.g., React, NextJS, Firebase)

### Setup

To set up the client:

1. Navigate to the client folder:

    ```bash
    cd client
    ```

2. Install the dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run dev
    ```

## Server

The server folder contains the backend code for the Cow Detection System. It handles video processing, object detection using YOLO, database interactions, and serves the API endpoints for the client.

### Dependencies

- Python 3.x
- Ultralytics YOLO
- OpenCV (`cv2`)
- Pyrebase
- Plyer
- Dotenv

### Setup

To set up the server:

1. Navigate to the server folder:

    ```bash
    cd server
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```


1. Ensure your webcam is connected or provide the path to your video file.
2. Run the Python script:

    ```bash
    python cattle_detection_with_single_video.py or
    python cattle_detection_with_multiple_video.py

    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
