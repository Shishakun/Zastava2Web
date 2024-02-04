<template>
  <div>
    <button @click="getVideoFeed">Get Video Feed</button>
    <video ref="video" width="640" height="480" autoplay></video>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'VideoFeed',
  data () {
    return {
      source: null
    }
  },
  methods: {
    async getVideoFeed () {
      this.updateVideoFeed()
      setInterval(this.updateVideoFeed, 1000)
    },
    async updateVideoFeed () {
      try {
        const response = await axios.get('http://localhost:8000/facerec/videofeed', {
          responseType: 'stream'
        })

        const reader = response.data.getReader()
        const decoder = new TextDecoder()

        while (true) {
          const { value, done } = await reader.read()

          if (done) {
            break
          }

          const boundary = '--frame\r\n'
          const boundaryIndex = value.indexOf(boundary)

          if (boundaryIndex > -1) {
            const frame = value.slice(0, boundaryIndex)
            const blob = new Blob([frame], { type: 'image/jpeg' })
            const url = URL.createObjectURL(blob)

            this.$refs.video.src = url
          }
        }
      } catch (error) {
        console.error('Error fetching video feed:', error)
      }
    }
  }
}
</script>
