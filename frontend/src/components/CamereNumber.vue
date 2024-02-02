<template>
  <div class="flex justify-center gap-2.5 mb-2 flex-wrap">
    <button
      v-for="i in 30"
      :key="i"
      :class="[
        'bg-[#272727] text-[#d5d5d5] items-center justify-center font-semibold rounded-xl px-2.5 py-1.5 duration-100 flex hover:bg-[#323232]',
        {
          'bg-whitesmoke text-[#272727] hover:bg-whitesmoke':
            activeButton === i,
        },
      ]"
      @click="handleButtonClick(i)"
    >
      Камера № {{ i }}
    </button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activeButton: null,
    };
  },
  methods: {
    handleButtonClick(cameraNumber) {
      if (this.activeButton === cameraNumber) {
        this.activeButton = null;
      } else {
        this.activeButton = cameraNumber;
      }
    },
  },
};
</script>
