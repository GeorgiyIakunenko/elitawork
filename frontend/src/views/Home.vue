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
    <div class="container">
      <section
        id="top"
        class="flex flex-col flex-wrap items-center justify-around sm:flex-row sm:flex-nowrap"
      >
        <div class="" data-aos="zoom-out-down">
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
          class="sm:max-h-72 lg:max-h-fit"
          src="@/assets/images/home-2-small.png"
        />
      </section>
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

@media (min-width: 768px) {
  #top {
    margin-top: -130px;
    min-height: calc(100vh);
  }
}
</style>