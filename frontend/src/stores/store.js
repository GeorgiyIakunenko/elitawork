import { ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("store", () => {
  const jobs = ref([
    {
      id: 1,
      name: "Frontend Developer",
      description:
        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
      type: "Full Time",
      salary: "£50,000 - £60,000",
    },
  ]);

  return {
    jobs,
  };
});
