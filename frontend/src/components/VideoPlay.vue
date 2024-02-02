<template>
  <div>
    <video ref="video" width="330" height="330" autoplay></video>
    <button>
      {{ webcamOn ? "Turn off webcam" : "Turn on webcam" }}
    </button>
  </div>
</template>
