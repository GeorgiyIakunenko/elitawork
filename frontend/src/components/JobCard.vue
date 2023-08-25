<script setup>
const props = defineProps({
  job: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div class="">
    <div>{{ job.name }}</div>
  </div>
</template>

<style scoped></style>
