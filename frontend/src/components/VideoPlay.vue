<template>
  <div>
    <video ref="video" width="330" height="330" autoplay></video>
    <button @click="toggleWebcam">
      {{ webcamOn ? "Turn off webcam" : "Turn on webcam" }}
    </button>
  </div>
</template>

<script>
import { WebSocket as WS } from "ws";
import face_recognition from "face-recognition";
import { face_confidence } from "./helpers";

export default {
  data() {
    return {
      webcamOn: false,
      ws: null,
      known_face_encodings: [],
      known_face_names: [],
      consecutive_detections: 0,
    };
  },
  methods: {
    async toggleWebcam() {
      if (this.webcamOn) {
        this.ws.close();
      } else {
        this.ws = new WS("ws://localhost:8000/webcam");
        this.ws.onopen = () => {
          console.log("WebSocket connected to webcam server");
        };
        this.ws.onmessage = async (event) => {
          const frame = new ImageData(
            new Uint8ClampedArray(event.data),
            330,
            330
          );
          const small_frame = this.$refs.video;
          small_frame.src = URL.createObjectURL(frame);
          small_frame.onload = async () => {
            const rgb_small_frame = this.convertToRGB(small_frame);
            const face_locations =
              face_recognition.face_locations(rgb_small_frame);
            const face_encodings = face_recognition.face_encodings(
              rgb_small_frame,
              face_locations
            );

            if (face_encodings.length > 0) {
              this.consecutive_detections += 1;
            } else {
              this.consecutive_detections = 0;
            }
            if (this.consecutive_detections >= 10) {
              console.error("ДОСТУП РАЗРЕШЕН");
            }

            const face_names = [];
            const image_path_acc = "";
            for (const face_encoding of face_encodings) {
              const matches = face_recognition.compare_faces(
                this.known_face_encodings,
                face_encoding
              );
              let name = "unknown";
              let confidence = "unknown";

              const face_distances = face_recognition.face_distance(
                this.known_face_encodings,
                face_encoding
              );
              const best_match_index = np.argmin(face_distances);

              if (matches[best_match_index]) {
                name = this.known_face_names[best_match_index];
                confidence = face_confidence(face_distances[best_match_index]);

                image_path_acc = `people\\${name}\\` + image;
              }

              face_names.push({ name, confidence });
            }
          };
        };
        this.ws.onclose = () => {
          console.log("WebSocket disconnected from webcam server");
        };
      }
      this.webcamOn = !this.webcamOn;
    },
    convertToRGB(image) {
      const canvas = document.createElement("canvas");
      canvas.width = image.width;
      canvas.height = image.height;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(image, 0, 0, image.width, image.height);
      const rgb_image = ctx.getImageData(0, 0, image.width, image.height);
      return rgb_image;
    },
  },
};
</script>
