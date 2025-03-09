import cv2
import pytest

def test_camera_connection():
    """Test if the camera can be opened and closed properly."""
    cap = cv2.VideoCapture(0)
    
    try:
        assert cap.isOpened(), "Camera failed to open"
        
        # Test if we can read at least one frame
        ret, frame = cap.read()
        assert ret, "Failed to read frame from camera"
        assert frame is not None, "Frame is None"
        assert frame.size > 0, "Frame is empty"
        
    finally:
        # Ensure camera is released even if test fails
        cap.release()
        cv2.destroyAllWindows()

@pytest.mark.manual
def manual_camera_test():
    """
    Manual test for visual inspection of camera feed.
    Run this separately from automated tests.
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        pytest.fail("Could not open camera.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                pytest.fail("Could not read frame.")

            cv2.imshow('Camera Test', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    manual_camera_test()