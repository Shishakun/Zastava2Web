<template>
  <div
    class="fixed xl:pt-3 inset-0 z-10 bg-black bg-opacity-75 focus:outline-none"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div class="bg-gray-200 px-4 mx-auto 2xl:w-[1080px] xl:my-2">
      <div class="flex justify-end p-2">
        <ModalWindowButtonClose @click="close" />
      </div>
      <div class="">
        <div
          class="flex transition flex-col justify-between py-2 pb-4 px-4 ml-2 mr-4 leading-normal"
        >
          <div class="border-b border-black" v-for="(item, index) in 10" :key="index">1</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  components: {
    ModalWindowButtonClose,
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
  props: {
    uav_img: String,
    uav_name: String,
    uav_country: String,
    uav_company: String,
    uav_endurance: Number,
    uav_range: Number,
    uav_payload: Number,
    uav_max_speed: Number,
    uav_platform: String,
    uav_altitude: String,
    uav_mass: Number,
    uav_width: Number,
    uav_length: Number,
  },
};
</script>
