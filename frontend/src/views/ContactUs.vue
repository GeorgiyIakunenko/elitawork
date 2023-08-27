<script setup>
import EmployeeCard from "@/components/EmployeeCard.vue";
import { useAppStore } from "@/stores/store";
import AOS from "aos";
import { onMounted } from "vue";
import { getEmployees } from "@/api/api";

const appStore = useAppStore();

onMounted(async () => {
  await getEmployees();
  AOS.init();
});
</script>

<template>
  <main>
    <div class="container">
      <div class="font-jost">
        <h1
          class="mb-12 text-center text-5xl font-medium text-neutral-700 lg:mb-24"
        >
          Наши контакты
        </h1>
        <div
          class="mx-auto flex flex-wrap justify-center gap-5 pb-10 lg:grid lg:grid-cols-3 lg:gap-10"
        >
          <EmployeeCard
            v-for="employee in appStore.employees"
            :employee="employee"
            data-aos="zoom-in-up"
            data-aos-duration="1000"
          ></EmployeeCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>