<template>
  <div class="flex">
    <div class="w-4/6 h-full">
      <CamereNumber />
      <div class="flex justify-center rounded-lg min-h-[750px] max-h-[750px] border-gray-500 border-[2px] mb-3">
        <VideoPlay />
      </div>
      <div>
        <YamnetOutput />
      </div>
    </div>
    <div class="w-2/6 px-4 h-full">
      <div class="flex flex-wrap gap-2 items-center mb-2">
        <input
          class="border-[#535353] text-whitesmoke border-[1.5px] px-2 py-2 rounded-xl bg-inherit"
          type="text"
          v-model="searchInput"
          placeholder="Поиск по дате"
        />
        <select
          class="border-[#535353] text-whitesmoke border-[1.5px] px-4 py-2 rounded-xl bg-[#0f0f0f]"
          v-model="selectedClass"
          @change="filterByClass"
        >
          <option value="" class="text-whitesmoke">Все классы</option>
          <option
            v-for="className in classList"
            class="bg-ingerit"
            :value="className"
          >
            {{ className }}
          </option>
        </select>
        <button
          class="border-[#535353] text-whitesmoke border-[1.5px] px-4 py-2 rounded-xl bg-[#0f0f0f] hover:bg-[#323232] duration-150"
        >
          Поиск
        </button>
      </div>
      <div
        class="border-[#535353] border-[1.5px] h-[883px] p-4 rounded-xl overflow-auto flex flex-col gap-4 custom-scrollbar"
      >
        <div
          v-for="item in filteredData"
          :key="item.id"
          class="flex gap-2.5 w-full"
        >
          <p class="text-white text-center w-1/6">{{ item.date }}</p>
          <div class="flex flex-col w-5/6">
            <p class="text-whitesmoke text-justify">{{ item.content }}</p>
            <img :src="item.image" class="pt-2" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CamereNumber from "./CamereNumber.vue";
import VideoPlay from "./VideoPlay.vue";
import YamnetOutput from "./YamnetOutput.vue";

export default {
  data() {
    return {
      activeButton: null,
      searchInput: "",
      data: [
        {
          id: 1,
          date: "10.11.2023 14:45",
          content:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae blanditiis officia quis nesciunt voluptatibus, suscipit inventore esse fuga temporibus saepe rerum sint sapiente, repellendus amet enim! Molestiae eius ipsam at?",
          image: "/img/222222.jpg",
          selectedClass: "Дрон",
        },
        {
          id: 1,
          date: "13.12.2021 11:55",
          content: "Обнаружено 3 позиции",
          image: "/img/222222.jpg",
          selectedClass: "Машина",
        },
      ],
      classList: ["Дрон", "Военная техника", "Машина", "Персона", "Оружие"], // список классов
    };
  },
  computed: {
    filteredData() {
      if (this.searchInput === "" && this.selectedClass === "") {
        return this.data;
      } else {
        return this.data.filter((item) => {
          const matchesSearch = item.date.includes(this.searchInput);
          const matchesClass =
            this.selectedClass === "" || item.class === this.selectedClass;
          return matchesSearch && matchesClass;
        });
      }
    },
  },
  methods: {
    handleButtonClick(cameraNumber) {
      if (this.activeButton === cameraNumber) {
        this.activeButton = null;
      } else {
        this.activeButton = cameraNumber;
      }
    },
    filterByClass() {
      this.searchInput = ""; // Сбросить поиск при изменении класса
    },
  },
  components: { VideoPlay, CamereNumber, YamnetOutput },
};
</script>

<style scoped>
button:focus {
  outline: none;
}
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #323232;
}
</style>
