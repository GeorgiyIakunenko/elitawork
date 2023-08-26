import { ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("store", () => {
  const jobs = ref([]);

  const setJobs = (data) => {
    jobs.value = data;
  };

  return {
    jobs,
    setJobs,
  };
});
