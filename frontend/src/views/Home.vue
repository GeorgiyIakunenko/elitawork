<script setup>
import JobCard from "@/components/JobCard.vue";
import { scrollToSection } from "@/components/scrollToElement";
import { onMounted } from "vue";
import { getJobs } from "@/api/api";
import { useAppStore } from "@/stores/store";
import Button from "@/components/Button.vue";

onMounted(async () => {
  await getJobs();
});
</script>

<template>
  <main class="scroll-smooth font-sans">
    <div class="container">
      <section id="top" class="flex flex-wrap items-center justify-around">
        <div class="">
          <div class="mb-4 md:mb-10">
            <h1 class="text-title font-bold">
              <span>Elita</span><span class="text-red-500">Work</span>
            </h1>
            <p class="text-lg text-neutral-700">Мы находим, вы выбираете!</p>
          </div>
          <Button @click="scrollToSection('jobs')">Смотреть вакансии</Button>
        </div>
        <img alt="" class="w-max" src="@/assets/images/home-image.jpg" />
      </section>

      <section id="jobs" class="text-center">
        <h2 class="mb-10 text-4xl font-bold text-red-500">Наши вакансии:</h2>
        <div
          class="mx-auto grid grid-cols-1 justify-center gap-3 gap-y-9 sm:grid-cols-2 md:gap-5 lg:grid-cols-3"
        >
          <JobCard v-for="job in useAppStore().jobs" :job="job"></JobCard>
        </div>
      </section>
      <a>scroll</a>
    </div>
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