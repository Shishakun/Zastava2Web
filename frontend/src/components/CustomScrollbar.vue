<template>
  <div class="custom-scrollbar">
    <div class="scrollbar-track">
      <div class="scrollbar-thumb"></div>
    </div>
    <div class="scrollbar-content">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.custom-scrollbar {
  position: relative;
  overflow: hidden;
}

.scrollbar-track {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 10px;
  background-color: #f1f1f1;
}

.scrollbar-thumb {
  width: 100%;
  background-color: #888;
}

.scrollbar-thumb:hover {
  background-color: #555;
}

.scrollbar-content {
  overflow-y: auto;
  margin-right: -10px;
  padding-right: 10px;
}
</style>
: создано с помощью chatgpt-russia.org
