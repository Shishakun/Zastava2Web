<template>
  <div class="flex gap-4 p-4">
    <div class="w-4/6 flex flex-col">
      <div
        class="flex justify-center h-[800px] border-gray-500 border-[2px] rounded-xl mb-3"
      >
        <VideoPlay />
      </div>
      <div class="flex w-full gap-2">
        <button
          class="bg-red-700 hover:bg-red-800 duration-150 text-whitesmoke font-semibold px-4 py-2 rounded-lg w-1/2"
        >
          Тревога
        </button>
        <button
          class="bg-green-700 hover:bg-green-800 duration-150 text-whitesmoke px-4 py-2 font-semibold rounded-lg w-1/2"
        >
          Пропустить
        </button>
      </div>
    </div>
    <div class="w-2/6">
      <div
        v-for="item in data"
        class="flex flex-col text-whitesmoke font-rale font-semibold text-xl gap-2"
      >
        <img
          :src="item.image"
          class="rounded-lg min-h-[750px] max-h-[750px] border-gray-500 border-[2px]"
        />
        <p>Воинское звание: {{ item.zvanie }}</p>
        <p>ФИО: {{ item.surname }} {{ item.name }} {{ item.otch }}</p>
        <p>Должность: {{ item.otdel }}</p>
      </div>
    </div>
  </div>
</template>
<script>
import VideoPlay from './VideoPlay.vue'
import axios from 'axios'

export default {
  data () {
    return {
      activeButton: null,
      searchInput: '',
      data: [
        {
          id: 1,
          image: '/img/111.jpg',
          zvanie: 'Полковник',
          surname: 'Шишкарев',
          name: 'Захар',
          otch: 'Андреевич',
          otdel: '1 отдел КККГЫРОС'
        }
      ]
    }
  },
  components: { VideoPlay }
}
</script>
