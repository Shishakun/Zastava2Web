<template>
  <div
    class="fixed xl:pt-3 inset-0 z-10 bg-black bg-opacity-75 focus:outline-none"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div
      class="bg-gray-900 text-whitesmoke px-4 mx-auto 2xl:w-[1080px] xl:my-2"
    >
      <div class="flex justify-end p-2">
        <ModalWindowButtonClose @click="close" />
      </div>
      <div class="">
        <div
          class="flex transition flex-col justify-between py-2 pb-4 px-4 ml-2 mr-4 leading-normal"
        >
          <form class="">
            <div class="flex-col items-center py-4">
              <div class="flex">
                <input
                  v-on:change="handleFilesUpload()"
                  class="w-full text-sm text-gray-700 border-[0.5px] py-1 px-2 border-[#e40046] rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
                  aria-describedby="file_input_help"
                  id="files"
                  ref="files"
                  type="file"
                />
                <p
                  class="mt-2.5 ml-2 text-sm text-gray-500"
                  id="file_input_help"
                >
                  .jpg
                </p>
              </div>
              <div class="flex-col p-4 text-whitesmoke">
                <div class="flex items-center border-b border-[#e40046] py-2">
                  <input
                    v-model="text"
                    @input="text_processing()"
                    class="appearance-none bg-transparent border-none w-full font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    placeholder="Воинское звание"
                    aria-label="Full name"
                  />
                </div>
                <div class="flex items-center border-b border-[#e40046] py-2">
                  <input
                    v-model="text"
                    @input="text_processing()"
                    class="appearance-none bg-transparent border-none w-full font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    placeholder="Фамилия"
                    aria-label="Surname"
                  />
                </div>
                <div class="flex items-center border-b border-[#e40046] py-2">
                  <input
                    v-model="text"
                    @input="text_processing()"
                    class="appearance-none bg-transparent border-none w-full font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    placeholder="Имя"
                    aria-label="Full name"
                  />
                </div>
                <div class="flex items-center border-b border-[#e40046] py-2">
                  <input
                    v-model="text"
                    @input="text_processing()"
                    class="appearance-none bg-transparent border-none w-full font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    placeholder="Отчество"
                    aria-label="Full name"
                  />
                </div>
                <div class="flex items-center border-b border-[#e40046] py-2">
                  <input
                    v-model="text"
                    @input="text_processing()"
                    class="appearance-none bg-transparent border-none w-full font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    placeholder="Должность"
                    aria-label="Full name"
                  />
                </div>
              </div>
            </div>
            <div class="flex justify-end pt-2">
              <button
                @click="submitFiles()"
                type="submit"
                class="text-whitesmoke bg-[#e40046] hover:bg-[#ce134b] focus:ring-4 focus:outline-none focus:ring-[#ce134b] font-semibold rounded-lg text-sm w-full sm:w-auto px-4 py-2.5 text-center mt-2"
              >
                Сохранить
              </button>
            </div>
          </form>
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
};
</script>
