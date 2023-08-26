<script setup>
import JobCard from "@/components/JobCard.vue";
import { useAppStore } from "@/stores/store";
import router from "@/router";
import { onMounted } from "vue";
import { getJobs } from "@/api/api";

const appStore = useAppStore();

const id = router.currentRoute.value.params.id;

onMounted(async () => {
  await getJobs();
  appStore.getCurrentJob(id);
  console.log(appStore.currentJob);
});
</script>

<template>
  <main>
    <div class="container">
      <div class="">
        <button
          class="btn mb-5 ml-auto w-fit rounded-xl bg-red-500 px-3.5 py-2 text-primary-white"
          @click="() => router.push({ name: 'homeJobs' })"
        >
          Вернуться назад
        </button>
        <h1 class="mb-10 text-center text-3xl">Наши вакансии</h1>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <JobCard :job="appStore.currentJob"></JobCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>