<script setup>
import JobCard from "@/components/JobCard.vue";
import { onMounted, ref } from "vue";
import { useAppStore } from "@/stores/store";
import axios from "axios";

const jobs = ref([]);

function getJobs() {
  return axios
    .get("http://elitawork.yuriipalamarchuk.com/api/v1/positions/")
    .then((response) => response.data)
    .catch((error) => {
      throw error; // Rethrow the error to be caught in the caller function
    });
}

const store = useAppStore();

onMounted(async () => {
  try {
    const res = await getJobs();
    console.log(res);
    jobs.value = res;
  } catch (error) {
    console.error("An error occurred while fetching jobs:", error);
  }
});

// Query
</script>

<template>
  <main>
    <div class="container">
      <div class="">
        <h1>Наши вакансии</h1>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <JobCard v-for="job in jobs" :job="job"></JobCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>