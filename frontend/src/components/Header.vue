<template>
  <nav
    class="bg-[#0f0f0f] py-4 px-16 flex justify-between items-center border-b-[1px] border-gray-600"
  >
    <a
      class="font-bold uppercase text-6xl cursor-pointer text-whitesmoke hover:text-red-700 duration-100 font-rale"
      href="/"
    >
      Застава
    </a>
    <div class="text-whitesmoke flex gap-4 font-monster text-xl font-bold">
      <router-link
        to="/"
        class="hover:text-gray-300 duration-150 animated-underline-red"
        :class="{ 'text-red-400': $route.path === '/' }"
      >
        Обнаружение объектов
      </router-link>
      <router-link
        to="/facerec"
        class="hover:text-gray-300 duration-150 animated-underline-gray"
        :class="{ 'text-red-400': $route.path === '/face_recognition' }"
      >
        Распознавание лиц
      </router-link>
      <router-link
        to="/database"
        class="hover:text-gray-300 duration-150 animated-underline-gray"
      >
        База данных
      </router-link>
    </div>
  </nav>
</template>

<style scoped>
.animated-underline-red {
  position: relative;
  display: inline-block;
  padding-bottom: 4px;
}

.animated-underline-red::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: red;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.3s ease-in-out;
}

.animated-underline-red:hover::before,
.active-red .animated-underline-red::before {
  transform: scaleX(1);
  transform-origin: left;
}

.animated-underline-gray {
  position: relative;
  display: inline-block;
  padding-bottom: 4px;
}

.animated-underline-gray::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: gray;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.3s ease-in-out;
}

.animated-underline-gray:hover::before,
.active-gray .animated-underline-gray::before {
  transform: scaleX(1);
  transform-origin: left;
}
</style>
