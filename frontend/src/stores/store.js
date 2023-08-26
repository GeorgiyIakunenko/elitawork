import { reactive, ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("store", {
  state: () => {
    const jobs = ref([]);
    const currentJob = reactive({
      id: 0,
      slug: "",
      name: "",
      important: false,
      picture: "",
      salary: "",
      location: "",
      note: "",
      description: "",
      managers: [],
    });
    const setCurrentJob = (job) => {
      currentJob.id = job.id;
      currentJob.slug = job.slug;
      currentJob.name = job.name;
      currentJob.important = job.important;
      currentJob.picture = job.picture;
      currentJob.salary = job.salary;
      currentJob.location = job.location;
      currentJob.note = job.note;
      currentJob.description = job.description;
      currentJob.managers = job.managers;
    };
    const setJobs = (data) => {
      jobs.value = data;
    };
    const getCurrentJob = (id) => {
      const foundJob = jobs.value.find(
        (job) => job.id.toString() === id.toString(),
      );
      if (foundJob) {
        setCurrentJob(foundJob);
      }
    };

    const employees = ref([]);

    const setEmployees = (data) => {
      employees.value = data;
    };

    return {
      jobs,
      setJobs,
      getCurrentJob,
      setCurrentJob,
      currentJob,
      employees,
      setEmployees,
    };
  },
});
