import os
import cv2
import face_recognition
import numpy as np
import logging
import matplotlib.pyplot as plt


def face_confidence(face_distance, face_match_threshold=0.6):
    range = 1.0 - face_match_threshold
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return round(linear_val * 100, 2)
    else:
        value = (
            linear_val + ((1.0 - linear_val) *
                          np.power((linear_val - 0.5) * 2, 0.2))
        ) * 100
        return round(value, 2) + '%'


# Create logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class FaceRecognition:
    # Load known faces
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        # Load images from 'people' directory
        for image in os.listdir('people'):
            face_image = face_recognition.load_image_file(f'people/{image}')
            face_encoding = face_recognition.face_encodings(face_image)[
                0]
            logger.debug(face_encoding)
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
            logger.debug(self.known_face_names)
    def run_recognition(self):
        # Initialize video capture
        video_capture_face_recognition = cv2.VideoCapture(0)
        logger.debug('Камера запущена')
        # Initialize consecutive detections counter
        logger.debug(video_capture_face_recognition)
        consecutive_detections = 0

        while True:
            ret, frame = video_capture_face_recognition.read()

            if self.process_current_frame:
                # Resize frame
                small_frame = cv2.resize(frame, (330, 330), fx=0.25, fy=0.25)

                # Convert to RGB
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Detect faces
                self.face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, self.face_locations
                )

                # Update consecutive detections counter
                if len(self.face_encodings) > 0:
                    consecutive_detections += 1
                else:
                    consecutive_detections = 0

                # Check if access should be granted
                if consecutive_detections >= 10:
                    logger.error("ДОСТУП РАЗРЕШЕН")

                # Initialize face names list
                face_names = []

                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(
                        self.known_face_encodings, face_encoding)

                    # Initialize name and confidence
                    name = "unknown"
                    confidence = "unknown"

                    # Find matches
                    face_distances = face_recognition.face_distance(
                        self.known_face_encodings, face_encoding
                    )
                    best_match_index = np.argmin(face_distances)

                    # If match found, update name and confidence
                    if matches[best_match_index] < 0.6:
                        name = self.known_face_names[best_match_index]
                        confidence = face_confidence(
                            face_distances[best_match_index])

                    # Append face name to list
                    self.face_names.append(f"{name} ({confidence}%)")

            self.process_current_frame = not self.process_current_frame
            # Draw rectangles around faces
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 1
                right *= 1
                bottom *= 1
                left *= 1

                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 255, 0), 1)
                # Display face name and confidence
                cv2.putText(
                    frame,
                    name,
                    (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_DUPLEX,
                    0.8,
                    (255, 255, 255),
                    1,
                )

                # Display frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) == ord('q'):
                break
        # Release video capture and close windows
        video_capture_face_recognition.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()
