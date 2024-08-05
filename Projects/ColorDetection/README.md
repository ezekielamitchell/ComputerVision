# Color Detection with OpenCV

This project demonstrates how to detect specific colors in a video stream using OpenCV. It captures video from the camera, converts the frames to HSV color space, applies a color mask, and draws bounding boxes around the detected colors.

## Requirements

- opencv-python==4.6.0.66
- numpy==1.23.4
- Pillow==9.2.0

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ezekielmitchell/color-detection-opencv.git
    cd Projects/ColorDetection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. Ensure your camera is connected.
2. Run the script:
    ```sh
    python main.py
    ```

## Usage

- The script will open a window displaying the video stream with bounding boxes around the detected colors. The default color is set to purple.
- Press `q` to quit the application.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

For any questions or suggestions, please contact [ezekiel@endrcompany.com](mailto:yezekiel@endrcompany.com).