<script setup>
import { useAppStore } from "@/stores/store";
import JobCard from "@/components/JobCard.vue";
import { useQuery } from "@tanstack/vue-query";

const store = useAppStore();

const { isLoading, isFetching, isError, data, error } = useQuery({
  queryKey: ["todos"],
  queryFn: () =>
    fetch("https://api.github.com/repos/TanStack/query").then((res) =>
      res.json(),
    ),
});

console.log(isLoading, isFetching, isError, data, error);
</script>

<template>
  <main>
    <div class="container">
      <div class="">
        <h1>Наши вакансии</h1>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <JobCard v-for="job in store.jobs" :job="job"></JobCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>