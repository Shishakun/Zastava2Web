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
            linear_val + ((1.0 - linear_val) * np.power((linear_val - 0.5) * 2, 0.2))
        ) * 100
        return round(value, 2)


# Create logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load known faces
known_face_encodings = []
known_face_names = []

# Load images from 'people' directory
people_folder = "people"
if os.path.isdir(people_folder):
    for folder in os.listdir(people_folder):
        folder_path = os.path.join(people_folder, folder)
        logger.debug(os.path.isdir(people_folder))
        logger.debug(folder_path)
        for image in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image)
            logger.debug(image_path)
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            logger.debug(face_encoding)

            known_face_encodings.append(face_encoding)
            known_face_names.append(folder)
            logger.debug(f"Loaded {image_path} for {folder}")
# Initialize video capture
video_capture_face_recognition = cv2.VideoCapture(0)
logger.debug('Камера запущена')
# Initialize consecutive detections counter
logger.debug(video_capture_face_recognition)
consecutive_detections = 0

while True:
    ret, frame = video_capture_face_recognition.read()

    if ret:
        # Resize frame
        small_frame = cv2.resize(frame, (330, 330), fx=0.25, fy=0.25)

        # Convert to RGB
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        # Update consecutive detections counter
        if len(face_encodings) > 0:
            consecutive_detections += 1
        else:
            consecutive_detections = 0

        # Check if access should be granted
        if consecutive_detections >= 10:
            logger.error("ДОСТУП РАЗРЕШЕН")

        # Initialize face names list
        face_names = []

        # Iterate over face encodings and locations
        for face_encoding, (top, right, bottom, left) in zip(
            face_encodings, face_locations
        ):
            # Initialize name and confidence
            name = "unknown"
            confidence = "unknown"

            # Find matches
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )
            best_match_index = np.argmin(face_distances)

            # If match found, update name and confidence
            if face_distances[best_match_index] < 0.6:
                name = known_face_names[best_match_index]
                confidence = face_confidence(face_distances[best_match_index])

            # Append face name to list
            face_names.append(f"{name} ({confidence}%)")

        # Draw rectangles around faces
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 1
            right *= 1
            bottom *= 1
            left *= 1

            cv2.rectangle(rgb_small_frame, (left, top), (right, bottom), (0, 255, 0), 1)

            # Display face name and confidence
            cv2.putText(
                rgb_small_frame,
                name,
                (left + 6, bottom - 6),
                cv2.FONT_HERSHEY_DUPLEX,
                0.5,
                (255, 255, 255),
                1,
            )

        # Display frame
        cv2.imshow('Video', rgb_small_frame)
        # Exit if 'q' key is pressed
        if cv2.waitKey(1):
            break

# Release video capture and close windows
video_capture_face_recognition.release()
cv2.destroyAllWindows()