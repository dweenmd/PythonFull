import cv2

# Initialize the camera
cam = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cam.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame")
        break

    # Display the frame in a window
    cv2.imshow('My Camera', frame)

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
