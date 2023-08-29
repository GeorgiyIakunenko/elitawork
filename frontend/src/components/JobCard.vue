<script setup>
import router from "@/router";

const props = defineProps({
  job: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div
    :class="{ 'bg-neutral-0': job.important }"
    class="relative z-10 flex min-w-full max-w-xl flex-col rounded-xl bg-white pb-5 font-primary shadow-md drop-shadow-xl transition-all duration-300 md:hover:scale-102"
  >
    <img
      :alt="job.name"
      :src="job.picture"
      class="mb-3 cursor-pointer rounded-xl object-contain"
      @click="() => router.push({ name: 'job', params: { slug: job.slug } })"
    />
    <div class="flex flex-grow flex-col px-4">
      <div class="mb-2 flex flex-grow justify-between text-start">
        <div class="mb-1 pl-1 text-xl font-medium">{{ job.name }}</div>
      </div>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2 text-sm">
          <img
            alt="location"
            class="h-5 w-5"
            src="@/assets/images/location.svg"
          />
          {{ job.location }}
        </div>
        <button
          class="btn ml-auto w-fit rounded-xl bg-red-500 px-3.5 py-2 text-primary-white transition-all duration-300 hover:scale-105 active:translate-y-1"
          @click="() => router.push({ name: 'job', params: { slug: job.slug } })"
        >
          Подробнее
        </button>
      </div>
    </div>
    <div
      class="absolute left-0 top-12 max-w-xl rounded-r-3xl bg-red-500 py-1 pl-2 pr-5 font-medium text-neutral-0"
    >
      {{ job.salary }}
    </div>
    <div
      v-if="job.important"
      class="absolute right-0 top-2 flex items-center gap-2 rounded-l-3xl bg-green-400 py-1 pl-3 pr-2 font-medium text-neutral-0"
    >
      Сейчас набор
      <img alt="time" class="h-6 w-6" src="@/assets/images/time.svg" />
    </div>
  </div>
</template>

<style scoped></style>