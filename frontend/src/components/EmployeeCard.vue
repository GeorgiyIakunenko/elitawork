<script setup>
import ContactIcon from "@/components/ContactIcon.vue";

const props = defineProps({
  employee: {
    type: Object,
    required: true,
  },
});

const contacts = props.employee.contacts;
</script>

<template>
  <div
    class="mx-auto flex w-fit flex-col items-center rounded object-contain p-2 font-jost sm:w-fit"
  >
    <img
      :alt="employee.name"
      :src="employee.photo"
      class="max-h-64 rounded-full lg:max-h-72"
    />
    <div class="mt-1 flex flex-col items-center justify-center gap-1 py-2">
      <div class="text-center">
        <a
          :href="employee.facebook"
          class="flex cursor-pointer items-center gap-1"
        >
          <h3 class="text-xl font-medium">{{ employee.name }}</h3>
          <img
            alt="facebook"
            class="h-6 w-6"
            src="@/assets/images/facebook.svg"
          />
        </a>
      </div>
      <div class="flex items-center gap-1 font-light">
        <img alt="job position" class="h-5 w-5" src="@/assets/images/job.svg" />
        {{ employee.job_position }}
      </div>

      <div class="flex flex-col items-center gap-1">
        <div
          v-for="contact in contacts"
          class="flex items-center gap-1 transition-all duration-300 hover:scale-105"
        >
          <a :href="'tel:' + contact.phone">{{ contact.phone }}</a>
          <div class="flex gap-2">
            <ContactIcon
              v-for="platform in contact.messenger_platforms"
              :phone="contact.phone"
              :platform="platform"
            >
            </ContactIcon>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>