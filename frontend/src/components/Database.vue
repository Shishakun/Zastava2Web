<template>
  <div class="h-screen">
    <div class="">
      <div class="flex justify-end px-24 pt-10">
        <button
          @click="isModalOpen = true"
          class="bg-green-700 hover:bg-green-800 duration-150 text-whitesmoke font-semibold px-4 py-2 rounded-lg w-1/6"
        >
          Добавить лицо
        </button>
      </div>
      <div class="px-24 py-4">
        <div
          class="p-4 border-2 border-gray-600 h-full grid grid-cols-2 rounded-lg gap-4"
        >
          <div
            v-for="item in data"
            class="flex text-whitesmoke font-rale font-semibold text-xl gap-4"
          >
            <img
              :src="item.image"
              class="rounded-lg max-h-[250px] border-gray-500 border-[2px]"
            />
            <div
              class="text-2xl tracking-widest pl-4 flex flex-col justify-between"
            >
              <div>
                <p>Воинское звание: {{ item.zvanie }}</p>
                <p>ФИО: {{ item.surname }} {{ item.name }} {{ item.otch }}</p>
                <p>Должность: {{ item.otdel }}</p>
              </div>
              <div class="flex justify-end">
                <button
                  class="bg-red-700 text-xl hover:bg-red-800 duration-150 text-whitesmoke font-semibold px-4 py-2 rounded-lg w-1/2"
                >
                  Удалить
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <ModalWindow
        :row_data="set_data"
        v-if="isModalOpen"
        @close="isModalOpen = false"
      />
    </div>
  </div>
</template>
<script>
import ModalWindow from "@/components/ModalWindow.vue";
export default {
  components: { ModalWindow },
  methods: {
    AddToDataBase: {},
  },
  data() {
    return {
      isModalOpen: false,
      emits: ["close"],
      activeButton: null,
      searchInput: "",
      data: [
        {
          id: 1,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
        {
          id: 2,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
        {
          id: 3,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
        {
          id: 4,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
        {
          id: 5,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
        {
          id: 6,
          image: "/img/111.jpg",
          zvanie: "Полковник",
          surname: "Шишкарев",
          name: "Захар",
          otch: "Андреевич",
          otdel: "1 отдел КККГЫРОС",
        },
      ],
    };
  },
};
</script>
