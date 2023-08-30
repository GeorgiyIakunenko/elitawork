<script setup>
import { useAppStore } from "@/stores/store";
import router from "@/router";
import { onMounted, reactive, ref } from "vue";
import { getEmployees, getJobs } from "@/api/api";
import EmployeeJobCard from "@/components/EmployeeJobCard.vue";
import { useHead } from "@vueuse/head";

const appStore = useAppStore();

const slug = router.currentRoute.value.params.slug;
const currentJob = reactive({ value: { managers: [] } });
let loading = ref(false);

onMounted(async () => {
  loading.value = true;
  await getJobs();
  await getEmployees();
  appStore.getCurrentJob(slug);
  currentJob.value = appStore.currentJob;
  //console.log(currentJob.value);
  useHead({
    title: "Вакансия " + currentJob.value.name + " - " + "Elita Work",
    meta: [
      {
        name: "description",
        content: currentJob.value.short_description,
      },
    ],
  });
  loading.value = false;
});
</script>

<template>
  <main>
    <div class="font-jost">
      <div class="container">
        <button
          class="btn mb-14 ml-auto w-fit rounded-xl bg-neutral-200 px-3.5 py-2 text-primary-white transition-all duration-300 hover:scale-105 active:translate-y-1"
          @click="() => router.push({ name: 'homeJobs' })"
        >
          Вернуться назад
        </button>
        <section v-if="!loading" class="mb-10 block lg:mb-24">
          <h1 class="mb-14 text-center text-5xl font-semibold text-neutral-700">
            {{ currentJob.value.name }}
          </h1>
          <div class="">
            <div class="mb-5 flex max-h-fit flex-col gap-3 px-1 md:flex-row">
              <div>
                <img
                  :alt="currentJob.value.name"
                  :src="currentJob.value.picture"
                  class="mb-4 w-full max-w-fit rounded-xl md:max-h-72 md:w-auto lg:max-h-96 lg:max-w-fit"
                />
                <div class="flex flex-col gap-2 px-2 text-lg md:px-0">
                  <div class="flex items-center font-medium">
                    <div>
                      <img
                        alt="location"
                        class="mr-2 h-5 w-5"
                        src="@/assets/images/location.svg"
                      />
                    </div>

                    <div>{{ currentJob.value.location }}</div>
                  </div>
                  <div class="flex items-center font-medium">
                    <img
                      alt="location"
                      class="mr-2 h-5 w-5"
                      src="@/assets/images/salary.svg"
                    />
                    <div>{{ currentJob.value.salary }}</div>
                  </div>
                </div>
              </div>
              <div class="flex flex-col px-2 lg:px-4">
                <div class="mb-6">
                  <div
                    class="text-justify"
                    v-html="$sanitize(currentJob.value.description)"
                  ></div>
                </div>
                <div v-if="currentJob.value.note">
                  <h3 class="text-md mb-2 text-start font-medium">
                    Примечания:
                  </h3>
                  <div class="w-4/5">
                    {{ currentJob.value.note }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <div
          v-if="loading"
          class="mt-20 flex flex-col items-center justify-center md:mb-20"
          role="status"
        >
          <svg
            aria-hidden="true"
            class="h-32 w-32 animate-spin fill-red-500 text-red-100 dark:text-gray-600"
            fill="none"
            viewBox="0 0 100 101"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
              fill="currentColor"
            />
            <path
              d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
              fill="currentFill"
            />
          </svg>
        </div>
        <hr
          v-if="!loading"
          class="my-6 border-gray-200 dark:border-gray-700 sm:mx-auto lg:my-8"
        />
      </div>

      <section v-if="!loading" class="">
        <div class="container">
          <h2 class="mb-4 text-center text-3xl font-semibold text-neutral-700">
            Заинтересовала вакансия?
          </h2>
          <div class="">
            <h5 class="mb-10 text-center text-sm text-neutral-700">
              Свяжитесь с нашими высококвалифицированными сотрудниками для
              трудоустройства
            </h5>
            <div
              :class="{
                'lg:grid-cols-3': currentJob.value.managers.length > 3,
              }"
              class="mx-auto flex w-fit flex-col flex-wrap items-center justify-center gap-5 pb-10 lg:grid lg:gap-10"
            >
              <EmployeeJobCard
                v-for="employee in currentJob.value.managers"
                :employee="employee"
                class="ml-0"
              ></EmployeeJobCard>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped></style>