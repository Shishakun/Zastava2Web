import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "objectDetection",

    component: () => import("../views/ObjectDetectionPage.vue"),
  },
  {
    path: "/face_recognition",
    name: "facerec",

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
