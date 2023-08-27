<script setup>
import { useAppStore } from "@/stores/store";
import router from "@/router";
import { onMounted, reactive, ref } from "vue";
import { getEmployees, getJobs } from "@/api/api";
import EmployeeJobCard from "@/components/EmployeeJobCard.vue";

const appStore = useAppStore();

const id = router.currentRoute.value.params.id;
const currentJob = reactive({ value: { managers: [] } });
let loading = ref(false);

onMounted(async () => {
  loading.value = true;
  await getJobs();
  await getEmployees();
  appStore.getCurrentJob(id);
  currentJob.value = appStore.currentJob;
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
                  <div class="text-justify">
                    {{ currentJob.value.description }}
                  </div>
                </div>
                <div class="">
                  <h3 class="mb-5 text-start text-2xl font-medium">
                    Примечания:
                  </h3>
                  <div class="w-4/5 text-justify">
                    {{ currentJob.value.note }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
      <hr
        v-if="!loading"
        class="my-6 border-gray-200 dark:border-gray-700 sm:mx-auto lg:my-8"
      />
      <section v-if="!loading" class="">
        <div class="container">
          <h2 class="mb-4 text-center text-3xl font-semibold text-neutral-700">
            Заинтересовала вакансия?
          </h2>
          <div class="">
            <h5 class="mb-10 text-center text-sm text-neutral-700">
              - Свяжитесь с нащими высококвалифицированными сотрудниками для:
              трудоустройства
            </h5>
            <div
              :class="{
                'lg:grid-cols-3': currentJob.value.managers.length > 3,
              }"
              class="mx-auto flex flex-wrap justify-center gap-5 pb-10 lg:grid lg:gap-10"
            >
              <EmployeeJobCard
                v-for="employee in currentJob.value.managers"
                :employee="employee"
              ></EmployeeJobCard>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped></style>