<script setup>
import { useAppStore } from "@/stores/store";
import router from "@/router";
import { onMounted, reactive } from "vue";
import { getEmployees, getJobs } from "@/api/api";
import EmployeeCard from "@/components/EmployeeCard.vue";

const appStore = useAppStore();

const id = router.currentRoute.value.params.id;
const currentJob = reactive({ value: {} });

onMounted(async () => {
  await getJobs();
  await getEmployees();
  appStore.getCurrentJob(id);
  currentJob.value = appStore.currentJob;
});
</script>

<template>
  <main>
    <div class="container">
      <div class="font-jost">
        <button
          class="btn mb-5 ml-auto w-fit rounded-xl bg-red-500 px-3.5 py-2 text-primary-white"
          @click="() => router.push({ name: 'homeJobs' })"
        >
          Вернуться назад
        </button>
        <section class="mb-10 block lg:mb-20">
          <h1 class="mb-10 text-center text-3xl font-medium text-neutral-700">
            {{ currentJob.value.name }}
          </h1>
          <div v-if="currentJob.value" class="">
            <div
              class="mb-5 flex max-h-fit flex-col gap-3 px-1 lg:block"
              style="min-height: 24rem"
            >
              <img
                :alt="currentJob.value.name"
                :src="currentJob.value.picture"
                class="mb-2 max-h-96 max-w-fit rounded-xl lg:float-left lg:mr-5 lg:mr-7 lg:max-w-fit"
              />
              <div>
                <div class="mb-2 flex items-center font-medium">
                  <img
                    v-if="currentJob.value.salary"
                    alt="location"
                    class="h-5 w-5"
                    src="@/assets/images/salary.svg"
                  />
                  <div>{{ currentJob.value.salary }}</div>
                </div>
                <div class="mb-5 flex items-center font-medium">
                  <img
                    v-if="currentJob.value.location"
                    alt="location"
                    class="h-5 w-5"
                    src="@/assets/images/location.svg"
                  />
                  <div>{{ currentJob.value.location }}</div>
                </div>
                <div class="mb-3">
                  <h3 class="mb-2 text-lg font-medium">Описание:</h3>
                  <div class="indent-5">
                    {{ currentJob.value.description }}
                  </div>
                </div>
                <div v-if="currentJob.value.note" class="px-3">
                  <h3 class="mb-2 text-start text-lg font-medium">
                    Примечания:
                  </h3>
                  <div class="inline indent-5">{{ currentJob.value.note }}</div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="">
          <h2 class="mb-4 text-center text-3xl font-medium text-neutral-700">
            Заинтересовала вакансия?
          </h2>
          <div class="">
            <h5 class="mb-3 text-center text-xl text-neutral-700">
              Связаться с нами:
            </h5>
            <div
              class="mx-auto flex flex-wrap justify-center gap-5 pb-10 lg:grid lg:grid-cols-3 lg:gap-10"
            >
              <EmployeeCard
                v-for="employee in appStore.employees"
                :employee="employee"
              ></EmployeeCard>
            </div>
          </div>
        </section>
      </div>
    </div>
  </main>
</template>

<style scoped></style>