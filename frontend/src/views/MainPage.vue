<template>
  <body class="">
    <Header></Header>
    <div class="bg-[#0f0f0f]">
      <div class="px-16 py-8">
        <objectDetection />
      </div>
      <Footer></Footer>
    </div>
  </body>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "../components/Footer.vue";
import objectDetection from "@/components/objectDetection.vue";
export default {
  components: { Header, Footer, objectDetection },
};
</script>

<style></style>
