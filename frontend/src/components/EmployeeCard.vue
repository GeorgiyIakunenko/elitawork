<script setup>
const props = defineProps({
  employee: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div
    class="max-w-64 mx-auto flex flex-col items-center rounded object-contain p-2 font-sans sm:w-fit"
  >
    <!-- Added "items-center" class -->
    <img
      :alt="employee.name"
      :src="employee.photo"
      class="max-h-64 rounded-full lg:max-h-72"
    />
    <div
      class="mt-1 flex h-24 max-h-36 w-full flex-col items-center gap-1 rounded-t-full bg-neutral-40 px-4 py-2"
    >
      <div class="text-center">
        <div class="">{{ employee.job_position }}</div>
        <h3 class="text-lg">{{ employee.name }}</h3>
      </div>
      <div class=""></div>
      <div class="">
        <a v-for="contact in employee.contacts" href="">{{ contact.phone }}</a>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
