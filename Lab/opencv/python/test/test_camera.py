import cv2

def test_camera():
    # Open the first camera connected to the computer
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return False

    while True:
        # Capture a frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame in a window
        cv2.imshow('Camera Test', frame)
        
        # Check if a key has been pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    return True

if __name__ == "__main__":
    if test_camera():
        print("Camera test passed.")
    else:
        print("Camera test failed.")