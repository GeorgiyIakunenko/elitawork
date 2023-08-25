<script setup>
import JobCard from "@/components/JobCard.vue";
</script>

<template>
  <main class="font-sans">
    <div class="container">
      <div class="flex flex-wrap items-center justify-around">
        <div class="">
          <div class="mb-4">
            <h1 class="font-bold" style="font-size: 60px">
              <span class="text-red-500">Elita</span> <span>work</span>
            </h1>
            <p class="text-lg text-neutral-700">Мы находим, вы выбираете</p>
          </div>

          <button
            class="btn rounded-xl bg-red-500 px-3.5 py-2 text-primary-white"
          >
            Смотреть вакансии
          </button>
        </div>
        <img alt="" class="w-max" src="@/assets/images/home-image.jpg" />
      </div>

      <section class="text-center">
        <div class="">Вакансии:</div>
        <div>
          <JobCard :job="{ name: 'kifli' }"></JobCard>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped></style>