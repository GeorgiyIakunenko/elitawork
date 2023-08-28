<script setup>
import { ref } from "vue";
import router from "@/router";
import Button from "@/components/Button.vue";
import { scrollToSection } from "@/components/scrollToElement";

const menuActive = ref(false);

const toggleMenu = () => {
  menuActive.value = !menuActive.value;
};
const CloseMenu = () => {
  menuActive.value = false;
};

const a = 0;

console.log(a);

const isRouteActive = (routeName, isButton = false) => {
  const currentRoute = router.currentRoute.value.name;
  console.log(currentRoute, routeName.toLowerCase());

  if (currentRoute === routeName) {
    return "link-active ";
  }

  if (isButton) {
    return "";
  }

  return "hover:text-red-500 transition-all";
};

const pushToJob = () => {
  if (router.currentRoute.value.name === "homeJobs") {
    scrollToSection("jobsSection", true);
  } else {
    router.push({ name: "homeJobs" });
  }

  CloseMenu();
};
</script>

<template>
  <header
    class="fixed left-0 right-0 top-0 bg-primary-white py-3 font-jost shadow-md"
  >
    <div class="container">
      <div class="wrapper flex items-center justify-between">
        <div
          class="z-20 cursor-pointer transition-all duration-300 hover:scale-105"
        >
          <div class="m-1">
            <router-link to="/" @click="CloseMenu">
              <img alt="logo" class="h-12" src="@/assets/images/logo.png" />
            </router-link>
          </div>
        </div>

        <div class="flex items-center gap-12">
          <nav
            :class="{ active: menuActive }"
            class="menu rounded-e-xl shadow-2xl max-[768px]:bg-neutral-0 md:max-w-none"
          >
            <ul
              class="mt-12 flex gap-3 font-medium text-primary-black md:mt-0 md:gap-12"
            >
              <li
                :class="isRouteActive('homeJobs')"
                class="relative cursor-pointer"
                @click="pushToJob"
              >
                Вакансии
                <div class="link__underline"></div>
              </li>
              <li :class="isRouteActive('about')" class="relative">
                <router-link class="relative" to="/about" @click="CloseMenu">
                  О нас
                </router-link>
                <div class="link__underline"></div>
              </li>
            </ul>
          </nav>
          <div class="left-block flex items-center gap-5">
            <div class="user-box flex items-center gap-5">
              <router-link class="" to="/contact">
                <Button>Связаться с нами</Button>
              </router-link>
            </div>
            <div
              :class="{ active: menuActive }"
              class="menu-burger md:hidden"
              @click="toggleMenu"
            >
              <span class="bg-primary-black"></span>
              <span class="bg-primary-black"></span>
              <span class="bg-primary-black"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  z-index: 101;
  height: 80px;
}

.link__underline {
  position: absolute;
  width: 0;
  left: 0;
  bottom: -4px;
  height: 2px;
  background-color: #ff0000;
  transition: all 0.3s ease-in-out;
}

li:hover .link__underline {
  width: 100%;
}

.link-active .link__underline {
  width: 100%;
}

/* Menu burger */

.menu-burger {
  position: relative;
  width: 30px;
  height: 30px;
  padding: 0;
  background-color: transparent;
  border: none;
  cursor: pointer;
  outline: 0;
  transition: all 0.3s ease-in-out;
}

.menu-burger span {
  position: absolute;
  width: 100%;
  height: 2px;
  transition: all 0.3s ease-in-out;
}

.menu-burger span:nth-child(1) {
  top: 0;
}

.menu-burger span:nth-child(2) {
  top: 50%;
  transform: translateY(-50%);
}

.menu-burger span:nth-child(3) {
  bottom: 0;
}

.menu-burger.active span:nth-child(1) {
  top: calc(50% - 1px);
  transform: rotate(45deg);
}

.menu-burger.active span:nth-child(2) {
  opacity: 0;
}

.menu-burger.active span:nth-child(3) {
  bottom: calc(50% - 1px);
  transform: rotate(-45deg);
}

@media (max-width: 768px) {
  .menu {
    transform: translateX(-250%);
    transition: all 0.3s ease-in-out;
    left: 0;
    top: 0;
    bottom: 0;
    position: fixed;
  }

  nav {
    min-width: 100%;
    background-color: rgba(255, 255, 255, 0.97);
  }

  .menu.active {
    transform: translateX(0);
  }

  .menu ul {
    flex-direction: column;
    justify-content: start;
    align-items: start;
    padding: 100px 20px 50px 50px;
    height: 100%;
    font-size: 40px;
    grid-gap: 55px;
  }
}
</style>