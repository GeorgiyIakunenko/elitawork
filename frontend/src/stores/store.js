import { ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("store", () => {
  const jobs = ref([]);

  const setJobs = (data) => {
    jobs.value = data;
  };

  const getJobById = (id) => {
    console.log(id);
    console.log(jobs.value);
    return jobs.value.forEach((job) => {
      if (job.id === id) {
        return job;
      }
    });
  };

  return {
    jobs,
    setJobs,
    getJobById,
  };
});
