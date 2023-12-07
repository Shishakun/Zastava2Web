<template>
  <div class="flex justify-left p-4">
    <canvas ref="canvasElement" class="shadow-2xl"></canvas>
  </div>
</template>

<script>
export default {
  mounted() {
    const canvas = this.$refs.canvasElement;

    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        const video = document.createElement("video");
        video.srcObject = stream;
        video.play();

        const context = canvas.getContext("2d");

        const updateVideoFrame = () => {
          requestAnimationFrame(updateVideoFrame);

          canvas.width = video.videoWidth * 1.75;
          canvas.height = video.videoHeight * 1.75;

          context.drawImage(video, 0, 0, canvas.width, canvas.height);
        };

        updateVideoFrame();
      })
      .catch((error) => {
        console.log("Ошибка при получении доступа к веб-камере: ", error);
      });
  },
};
</script>
