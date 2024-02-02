import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",

    component: () => import("../views/MainPage.vue"),
  },
  {
    path: "/faceRecognition",
    name: "faceRecognition",

    component: () => import("../views/FaceRecognitionPage.vue"),
  },
  {
    path: "/database",
    name: "database",

    component: () => import("../views/Database.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
