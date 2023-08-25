<script setup>
import EmployeeCard from "@/components/EmployeeCard.vue";
</script>

<template>
  <main>
    <div class="container">
      <div class="font-roboto">
        <h1 class="mb-10 text-center font-bold" style="font-size: 2.5rem">
          Наши контакты
        </h1>
        <div
          class="mx-auto grid grid-cols-1 justify-center gap-3 sm:grid-cols-2 md:gap-4 lg:grid-cols-3 lg:gap-4"
        >
          <EmployeeCard></EmployeeCard>
          <EmployeeCard></EmployeeCard>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>