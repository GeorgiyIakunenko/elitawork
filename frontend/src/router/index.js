import { createRouter, createWebHistory } from "vue-router";
import { scrollToSection } from "@/components/scrollToElement";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from) {
    if (to.name === "homeJobs") {
      scrollToSection("jobs");
      return;
    }

    if (to.name === "job") {
      return { top: 0 };
    }

    if (to.fullPath === "/" && from.path === "/") {
      console.log("home");
      return { top: 0, behavior: "smooth" };
    }

    return { top: 0, behavior: "smooth" };
  },
  routes: [
    {
      path: "/",
      name: "home",

      component: () => import("../views/Home.vue"),
    },
    {
      path: "/",
      name: "homeJobs",

      component: () => import("../views/Home.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/About.vue"),
    },
    {
      path: "/contact",
      name: "contact",
      component: () => import("../views/ContactUs.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: () => import("@/views/PageNotFound.vue"),
    },
    {
      path: "/job/:id",
      name: "job",
      component: () => import("../views/Job.vue"),
    },
  ],
});

export default router;
