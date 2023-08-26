<script setup>
import JobCard from "@/components/JobCard.vue";
import { useAppStore } from "@/stores/store";
import router from "@/router";
import { onMounted, ref } from "vue";
import { getJobs } from "@/api/api";

const appStore = useAppStore();

let job = ref({});

onMounted(async () => {
  await getJobs();
  job = appStore.jobs.find(
    (job) => job.id === router.currentRoute.value.params.id,
  );
});

// Query
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
          <JobCard :job="job"></JobCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>