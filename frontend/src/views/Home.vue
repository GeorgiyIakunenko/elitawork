<script setup>
import JobCard from "@/components/JobCard.vue";
import { nextTick, onMounted, ref } from "vue";
import { getJobs } from "@/api/api";
import { useAppStore } from "@/stores/store";
import AOS from "aos";
import Button from "@/components/Button.vue";
import { useHead } from "@vueuse/head";
import router from "@/router";
import { scrollToSection } from "@/components/scrollToElement";

const loading = ref(false);
onMounted(async () => {
  AOS.init();
  loading.value = true;
  await getJobs();
  useHead({
    title: "Вакансии" + " - " + "Elita Work",
    link: [],
    meta: [
      {
        name: "description",
        content:
          "Наши вакансии. Мы находим, вы выбираете! Присоединяйтесь к нашей команде профессионалов и найдите идеальную вакансию.",
      },
    ],
  });
  loading.value = false;

  await nextTick(() => {
    if (router.currentRoute.value.name === "homeJobs") {
      scrollToSection("jobsSection", true);
    }
  });
});
</script>

<template>
  <main class="scroll-smooth font-primary">
    <div class="top">
      <div class="container">
        <section
          id="top"
          class="flex flex-col flex-wrap items-center sm:flex-row sm:flex-nowrap md:justify-center"
        >
          <div class="main-content mr-auto md" data-aos="zoom-out-down">
            <div class="mb-4 md:mb-10">
              <h1 class="text-7xl font-bold lg:text-9xl">
                <span>Elita</span><span class="text-red-500">Work</span>
              </h1>
              <p class="pl-2 text-lg text-neutral-700 lg:pl-2 lg:text-2xl">
                Мы находим, вы выбираете!
              </p>
            </div>
            <Button
              class="ml-3 px-7 py-3 text-lg"
              @click="scrollToSection('jobsSection')"
              >Смотреть вакансии
            </Button>
          </div>
        </section>
      </div>
    </div>

    <section
      id="jobsSection"
      class="-mt-24 pt-24 text-center font-primary lg:mb-20"
    >
      <div class="container">
        <h2 class="mb-14 text-4xl font-bold text-red-500 lg:mb-16">
          Наши вакансии:
        </h2>
        <div
          v-if="!loading"
          class="mx-auto grid grid-cols-1 justify-center gap-3 gap-y-9 sm:grid-cols-2 md:gap-5 lg:grid-cols-3"
        >
          <JobCard v-for="job in useAppStore().jobs" :job="job"></JobCard>
        </div>
        <div
          v-if="loading"
          class="mt-20 flex flex-col items-center justify-center md:mb-20"
          role="status"
        >
          <svg
            aria-hidden="true"
            class="h-32 w-32 animate-spin fill-red-500 text-red-100 dark:text-gray-600"
            fill="none"
            viewBox="0 0 100 101"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
              fill="currentColor"
            />
            <path
              d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
              fill="currentFill"
            />
          </svg>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
#top {
  min-height: calc(100vh - 100px);
}

.top {
  background-image: url("@/assets/images/home-full.png");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center 65%;
}

@media (min-width: 640px) {
  .top {
    background-position: right;
    background-size: 45%;
  }
}

@media (max-width: 640px) {
  .main-content {
    margin-top: 20%;
  }
}

@media (min-width: 1400px) {
  .top {
    background-position: right;
    background-size: 40%;
  }
}

@media (min-width: 768px) {
  #top {
    margin-top: -130px;
    min-height: calc(100vh);
  }
}
</style>