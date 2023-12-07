<template>
  <aside>
    <div
      class="sm:w-64 w-full h-72 flex flex-col overflow-auto bg-gradient-to-b from-cyan-400 to-blue-600 fixed z-40 outline-none"
    >
      <div class="flex justify-end items-center p-4">
        <button>
          <BaseIcon name="x" class="h-6 w-6 text-whitesmoke" />
        </button>
      </div>
      <div class="flex flex-col justify-center text-center gap-2 pt-8 px-4">
        <router-link
          to=""
          class="border-b-gray-200 border-b-[1px] text-whitesmoke font-rale font-semibold tracking-widest"
          >Статистика</router-link
        >
        <router-link
          to=""
          class="border-b-gray-200 border-b-[1px] text-whitesmoke font-rale font-semibold tracking-widest"
          >База данных</router-link
        >
        <router-link
          to=""
          class="border-b-gray-200 border-b-[1px] text-whitesmoke font-rale font-semibold tracking-widest"
          >Инструкция к применению</router-link
        >
      </div>
    </div>
  </aside>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: {
    BaseIcon,
  },
};
</script>
