import cv2
import numpy as np

def process_frame(frame):
    # Flip the frame horizontally and convert to grayscale
    # gray_frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve corner detection
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Convert to float32
    gray = np.float32(gray_frame)

    # Apply Harris Corner Detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Dilate the result to mark the corners
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image
    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    return frame

def main():
    stream = cv2.VideoCapture(0)

    if not stream.isOpened():
        print("Error: Could not open video stream")
        return

    try:
        while True:
            ret, frame = stream.read()

            if not ret:
                print("Failed to capture image")
                break

            # Process the frame
            result_frame = process_frame(frame)

            # Display the result
            cv2.imshow('Corners', result_frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(3) & 0xFF == ord('q'):
                break
    finally:
        # Release the video capture object and close all OpenCV windows
        stream.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
