<script setup>
import EmployeeCard from "@/components/EmployeeCard.vue";
import { useAppStore } from "@/stores/store";
import { onMounted, ref } from "vue";
import { getEmployees } from "@/api/api";
import AOS from "aos";

const appStore = useAppStore();
const loading = ref(false);
onMounted(async () => {
  loading.value = true;
  await getEmployees();
  AOS.init();
  loading.value = false;
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
          v-if="!loading"
          class="mx-auto flex flex-wrap justify-center gap-5 pb-10 lg:grid lg:grid-cols-3 lg:gap-10"
        >
          <EmployeeCard
            v-for="employee in appStore.employees"
            :employee="employee"
            data-aos="fade-up"
            data-aos-duration="1000"
          ></EmployeeCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>