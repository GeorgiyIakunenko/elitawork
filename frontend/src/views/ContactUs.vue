<script setup>
import EmployeeCard from "@/components/EmployeeCard.vue";
import { useAppStore } from "@/stores/store";
import { onMounted } from "vue";
import { getEmployees } from "@/api/api";

const appStore = useAppStore();

onMounted(async () => {
  await getEmployees();
});
</script>

<template>
  <main>
    <div class="container">
      <div class="font-roboto">
        <h1 class="mb-24 text-center font-bold" style="font-size: 2.5rem">
          Наши контакты
        </h1>
        <div class="mx-auto flex flex-wrap justify-center gap-10 pb-10">
          <EmployeeCard
            v-for="employee in appStore.employees"
            :employee="employee"
          ></EmployeeCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>