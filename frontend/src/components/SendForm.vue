<template>
  <div>
    <form class="sm:max-w-xl max-w-xs px-2.5 sm:mx-auto pt-4">
      <div class="">
        <label
          for="username-success"
          class="block mb-2 sm:text-base text-sm font-medium text-gray-700"
          >Форма отправки сообщений</label
        >
        <input
          type="text"
          id="username-success"
          class="bg-gray-50 border border-blue-500 text-gray-900 placeholder-gray-700 sm:text-sm text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          placeholder="Введите текст"
        />
        <!-- <p class="mt-2 text-sm text-green-600">
          <span class="font-medium">Alright!</span> Username available!
        </p> -->
      </div>
      <!-- <div>
        <label
          for="username-error"
          class="block mb-2 text-sm font-medium text-red-700 dark:text-red-500"
          >Your name</label
        >
        <input
          type="text"
          id="username-error"
          class="bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 focus:border-red-500 block w-full p-2.5"
          placeholder="Bonnie Green"
        />
        <p class="mt-2 text-sm text-red-600">
          <span class="font-medium">Oops!</span> Username already taken!
        </p>
      </div> -->
    </form>
  </div>
</template>
<script>
export default {};
</script>
