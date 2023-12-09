import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",

    component: () =>
      import("../views/MainPage.vue"),
  },
  {
    path: "/face",
    name: "faceRecognition",

    component: () =>
      import("../views/FaceRecognitionPage.vue"),
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
