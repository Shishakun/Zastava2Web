<template>
  <body class="">
    <Header></Header>
    <div class="bg-[#0f0f0f]">
      <Database />
      <Footer></Footer>
    </div>
  </body>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "../components/Footer.vue";
import objectDetection from "@/components/objectDetection.vue";
import FaceRecognition from "@/components/faceRecognition.vue";
import Database from "@/components/Database.vue";
export default {
  components: { Header, Footer, objectDetection, FaceRecognition, Database },
};
</script>

<style></style>
