<template>
  <div class="max-h-[660px] w-full">
    <div class="flex justify-start w-full">
      <button
        class="bg-gray-700 hover:bg-gray-800 duration-150 text-whitesmoke px-4 py-2 w-1/4 font-semibold rounded-lg"
        @click="toggleWebcam"
      >
        {{ webcamOn ? 'Turn off webcam' : 'Turn on webcam' }}
      </button>
    </div>
    <video
      ref="video"
      autoplay
      playsinline
      :style="{ display: webcamOn ? 'block' : 'none' }"
    ></video>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  data () {
    return {
      webcamOn: false,
      videoStream: null
    }
  },
  methods: {
    async toggleWebcam () {
      if (!this.webcamOn) {
        try {
          const response = await axios.get('/video_feed', {
            responseType: 'stream'
          })
          this.videoStream = response.data
          this.$refs.video.srcObject = this.videoStream
          this.webcamOn = true
        } catch (error) {
          console.error('Error fetching video feed:', error)
        }
      } else {
        this.$refs.video.srcObject = null
        this.webcamOn = false
      }
    }
  }
}
</script>
