<template>
  <header>
    <nav class="bg-blue-700 py-4 px-6 flex justify-between items-center">
      <BaseIcon name="menu" class="w-6 h-6 text-whitesmoke" />
      <a class="text-gray-200 font-bold text-xs">{{ projectName }}</a>
    </nav>
  </header>
</template>

<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: {
    BaseIcon,
  },
  props: ["projectName"],
};
</script>
