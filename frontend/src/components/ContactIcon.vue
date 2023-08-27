<script setup>
import { computed } from "vue";

const props = defineProps({
  platform: {
    type: Object,
    required: true,
  },
  phone: {
    type: String,
    required: true,
  },
});

const platformName = props.platform.name.toLowerCase();

const link = computed(() => {
  return {
    telegram: "https://t.me/share?url=" + props.phone,
    whatsapp: "https://api.whatsapp.com/send?phone=" + props.phone,
    viber: "viber://add?number=" + props.phone,
    phone: "tel:" + props.phone,
    facebook: "https://m.me/" + props.phone,
  };
});
</script>

<template>
  <a :href="link[platformName]" class="">
    <img :alt="platform.name" :src="platform.logo" class="h-6 w-6" />
  </a>
</template>

<style scoped></style>