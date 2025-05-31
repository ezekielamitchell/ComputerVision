import cv2
import time
import platform

capture = cv2.VideoCapture(2) # grab default camera

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) # grab frame width
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) # grab frame height

fps = capture.get(cv2.CAP_PROP_FPS)
print(f'Camera FPS: {fps}')

window_name = f'Platform: {platform.system()}'
cv2.namedWindow(window_name)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter('test_video_0.mp4', fourcc, 30, (width, height))

prev_time = 0

while True:
    ret, frame = capture.read()
    if not ret: 
        break

    curr_time = time.time()
    real_time_fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
    prev_time = curr_time

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    display_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Create a blank image for the FPS text
    text_img = display_frame.copy()
    text_img[:] = 0  # Make it black

    # Draw FPS text on the blank image
    cv2.putText(text_img, f'FPS: {real_time_fps:.2f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Crop the region where the text is drawn
    text_roi = text_img[0:50, 0:250]  # Adjust size as needed

    # Flip the text ROI horizontally
    flipped_text = cv2.flip(text_roi, 1)

    # Place the flipped text back onto the display frame
    display_frame[0:50, 0:250] = flipped_text

    writer.write(frame)
    cv2.imshow(window_name, cv2.flip(display_frame,1))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
writer.release()
cv2.destroyAllWindows()