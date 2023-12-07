<template>
  <body class="">
    <Header></Header>
    <div class="">
      <ObjectDetection />
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import ObjectDetection from "@/components/objectDetection.vue";
export default {
  components: { Header, Footer, ObjectDetection },
};
</script>

<style></style>
