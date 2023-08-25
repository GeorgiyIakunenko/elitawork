<script setup>
import { ref } from "vue";
import router from "@/router";

const menuActive = ref(false);

const toggleMenu = () => {
  menuActive.value = !menuActive.value;
};
const CloseMenu = () => {
  menuActive.value = false;
};

const isRouteActive = (routeName, isButton = false) => {
  const currentRoute = router.currentRoute.value.name;

  //console.log(currentRoute, routeName)

  if (currentRoute === routeName.toLowerCase()) {
    return "font-bold ";
  }

  if (isButton) {
    return "";
  }

  return "hover:text-red-500 transition-all";
};
</script>

<template>
  <header
    class="fixed left-0 right-0 top-0 bg-primary-white py-3 font-sans shadow-md"
  >
    <div class="container">
      <div class="wrapper flex items-center justify-between">
        <div
          class="z-20 cursor-pointer p-1 transition-all duration-300 hover:scale-105"
        >
          <router-link to="/" @click="CloseMenu">
            <img alt="logo" class="h-12" src="@/assets/images/logo.png" />
          </router-link>
        </div>
        <nav
          :class="{ active: menuActive }"
          class="menu rounded-e-xl shadow-2xl max-[768px]:bg-neutral-0 md:max-w-none"
        >
          <ul
            class="mt-12 flex gap-3 font-medium text-primary-black md:mt-0 md:gap-12"
          >
            <li>
              <router-link
                :class="isRouteActive('Home')"
                to="/"
                @click="CloseMenu"
                >Домой
              </router-link>
            </li>
            <li>
              <router-link
                :class="isRouteActive('jobs')"
                to="/jobs"
                @click="CloseMenu"
              >
                Вакансии
              </router-link>
            </li>
            <li>
              <router-link
                :class="isRouteActive('about')"
                to="/about"
                @click="CloseMenu"
              >
                О нас
              </router-link>
            </li>
          </ul>
        </nav>
        <div class="left-block flex items-center gap-5">
          <div class="user-box flex items-center gap-5">
            <router-link class="rounded-xl bg-neutral-30 p-2" to="/contact">
              Связаться с нами
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
  </header>
</template>

<style scoped>
header {
  z-index: 10;
  height: 80px;
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
    align-items: center;
    padding: 100px 20px 50px 20px;
    height: 100%;
    font-size: 40px;
    grid-gap: 55px;
  }
}
</style>