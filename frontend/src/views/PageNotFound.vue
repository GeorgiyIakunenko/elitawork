<script lang="ts" setup></script>

<template>
  <main class="flex flex-col items-center justify-center py-24">
    <div class="flex flex-col items-center px-24">
      <div class="font-sans text-xl font-medium text-red-500">
        <img alt="page not found" class="mb-4" src="@/assets/images/404.svg" />
        Страница не найдена
      </div>
    </div>
    <router-link exact to="/">
      <button class="mt-5 rounded-xl bg-neutral-400 px-3.5 py-2 text-white">
        Вернуться на главную страницу
      </button>
    </router-link>
  </main>
</template>

<style scoped></style>
