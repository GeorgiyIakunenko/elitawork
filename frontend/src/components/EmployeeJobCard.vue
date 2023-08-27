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
    class="max-w-64 mx-auto flex items-center gap-3 rounded object-contain p-2 font-jost sm:w-fit"
  >
    <img
      :alt="employee.name"
      :src="employee.photo"
      class="max-h-20 rounded-full lg:max-h-20"
    />
    <div class="mt-1 flex h-24 flex-col items-start gap-1 py-2">
      <div class="text-start">
        <h3 class="text-xl font-medium">{{ employee.name }}</h3>
      </div>
      <div
        v-for="contact in contacts"
        class="flex items-center gap-1 transition-all duration-300 hover:scale-105"
      >
        <a :href="'tel:' + contact.phone">{{ contact.phone }}</a>
        <ContactIcon
          v-for="platform in contact.messenger_platforms"
          :phone="contact.phone"
          :platform="platform"
        >
        </ContactIcon>
      </div>
    </div>
  </div>
</template>

<style scoped></style>