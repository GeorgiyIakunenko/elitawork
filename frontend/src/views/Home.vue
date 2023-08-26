<script setup>
import JobCard from "@/components/JobCard.vue";
import { scrollToSection } from "@/components/scrollToElement";
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

          <button
            class="btn rounded-xl bg-red-500 px-3.5 py-2 text-primary-white"
            @click="scrollToSection('jobs')"
          >
            Смотреть вакансии
          </button>
        </div>
        <img alt="" class="w-max" src="@/assets/images/home-image.jpg" />
      </section>

      <section id="jobs" class="text-center">
        <h2 class="text-xl">Вакансии:</h2>
        <div>
          <JobCard :job="{ name: 'kifli' }"></JobCard>
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
        </div>
        <div class="mb-4 h-40 bg-neutral-200">
          dgasdgdfsgfds df sg sdf g sdfg d sfg sdf g sdfg sdf g dfs g s fg sd g
          sdg sd g fsd g dfs g
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