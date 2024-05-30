import cv2

class Camera:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)

    def capture_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            print("Error: Failed to capture frame.")
            return None

    def release(self):
        self.cap.release()

# Example usage:
if __name__ == "__main__":
    # Create a camera object
    camera = Camera()

    # Capture and display frames from the camera
    while True:
        frame = camera.capture_frame()
        if frame is not None:
            cv2.imshow("Camera Feed", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    camera.release()
    cv2.destroyAllWindows()
