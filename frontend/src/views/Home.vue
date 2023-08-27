<script setup>
import JobCard from "@/components/JobCard.vue";
import { scrollToSection } from "@/components/scrollToElement";
import { onMounted } from "vue";
import { getJobs } from "@/api/api";
import { useAppStore } from "@/stores/store";
import AOS from "aos";
import Button from "@/components/Button.vue";

onMounted(async () => {
  await getJobs();
  AOS.init();
});
</script>

<template>
  <main class="scroll-smooth font-sans">
    <div class="top">
      <div class="container">
        <section
          id="top"
          class="flex flex-col flex-wrap items-center justify-start sm:flex-row sm:flex-nowrap md:justify-center"
        >
          <div class="mr-auto md:ml-20" data-aos="zoom-out-down">
            <div class="mb-4 md:mb-10">
              <h1 class="text-title font-bold">
                <span>Elita</span><span class="text-red-500">Work</span>
              </h1>
              <p class="text-lg text-neutral-700">Мы находим, вы выбираете!</p>
            </div>
            <Button class="px-7 py-3 text-lg" @click="scrollToSection('jobs')"
              >Смотреть вакансии
            </Button>
          </div>
          <img
            alt="passports"
            class="hidden sm:max-h-72 lg:max-h-fit"
            src="@/assets/images/home-2-small.png"
          />
        </section>
      </div>
    </div>

    <section id="jobs" class="mb-10 text-center font-jost lg:mb-20">
      <div class="container">
        <h2 class="mb-14 text-4xl font-bold text-red-500 lg:mb-16">
          Наши вакансии:
        </h2>
        <div
          class="mx-auto grid grid-cols-1 justify-center gap-3 gap-y-9 sm:grid-cols-2 md:gap-5 lg:grid-cols-3"
        >
          <JobCard v-for="job in useAppStore().jobs" :job="job"></JobCard>
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
  background-image: url("@/assets/images/home-2-small.png");
  background-repeat: no-repeat;
  background-size: 60%;
  background-position: right;
}

@media (min-width: 640px) {
  .top {
    background-size: 50%;
  }
}

@media (min-width: 768px) {
  #top {
    margin-top: -130px;
    min-height: calc(100vh);
  }
}
</style>