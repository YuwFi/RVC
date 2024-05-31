import cv2
import numpy as np

class Preprocessing:
    def __init__(self, resize_shape=(224, 224)):
        self.resize_shape = resize_shape

    def preprocess_frame(self, frame):
        # Resize frame to specified shape
        resized_frame = cv2.resize(frame, self.resize_shape)

        # Convert frame to RGB format
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Normalize frame pixel values to range [0, 1]
        normalized_frame = rgb_frame / 255.0

        return normalized_frame

# Example usage:
if __name__ == "__main__":
    # Example frame
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)  # Random frame of size 640x480

    # Create a preprocessing object
    preprocessing = Preprocessing()

    # Preprocess the frame
    preprocessed_frame = preprocessing.preprocess_frame(frame)

    # Display original and preprocessed frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Preprocessed Frame", preprocessed_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
