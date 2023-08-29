<script setup>
import { onMounted, ref } from "vue";
import AOS from "aos";
import { useHead } from "@vueuse/head";
import { getPartners } from "@/api/api";

const partners = ref([]);
const loading = ref(false);

onMounted(async () => {
  AOS.init();
  useHead({
    title: "О нас" + " - " + "Elita Work",
    meta: [
      {
        name: "description",
        content:
          "Компания Elita Work - это инновационная и динамично развивающаяся организация, специализирующаяся в области трудоустройства, рекрутинга и управления персоналом.",
      },
    ],
  });
  loading.value = true;
  const res = await getPartners();
  if (res.success) {
    partners.value = res.data;
  }
  loading.value = false;
  console.log(partners.value);
});
</script>

<template>
  <main class="min-h-screen bg-gray-100 font-primary">
    <div class="container">
      <div class="rounded-lg bg-white p-8 shadow-md">
        <h1 class="mb-7 text-center text-3xl font-semibold md:mb-14">О нас</h1>
        <div
          class="mb-6 text-gray-600 md:mx-auto md:w-3/5"
          data-aos="fade-up"
          data-aos-duration="1000"
        >
          Компания Elita Work - это инновационная и динамично развивающаяся
          организация, специализирующаяся в области трудоустройства, рекрутинга
          и управления персоналом. С нашим богатым опытом и экспертизой в сфере
          человеческих ресурсов, мы стремимся предоставлять клиентам
          высококачественные решения для эффективного управления персоналом.
        </div>
        <div
          class="mb-5 md:mx-auto md:w-3/5"
          data-aos="fade-up"
          data-aos-duration="1000"
        >
          <div class="mb-4 flex items-center justify-center gap-3">
            <img alt="" class="h-12" src="@/assets/images/mission.svg" />
            <div class="text-lg">Наша миссия</div>
          </div>
          <div class="text-gray-600">
            Миссией Elita Work является соединение талантов и возможностей. Мы
            считаем, что успешное предприятие начинается с компетентных и
            мотивированных сотрудников. Наша цель - обеспечить клиентов
            надежными партнерами для поиска, подбора и развития профессионалов,
            способных внести вклад в достижение их корпоративных целей.
          </div>
        </div>
        <div
          v-if="!loading"
          class="md:mx-auto md:w-3/5"
          data-aos="fade-up"
          data-aos-duration="1000"
        >
          <div class="mb-7 flex items-center justify-center gap-3">
            <img alt="" class="h-12" src="@/assets/images/partners.svg" />
            <div class="text-lg">Наши партнеры</div>
          </div>
          <div class="flex flex-wrap justify-center gap-7 md:gap-10">
            <div
              v-for="partner in partners"
              class="flex flex-col items-center gap-4 lg:gap-7"
            >
              <a :href="partner.link" class="cursor-pointer"
                ><img
                  :alt="partner.name"
                  :src="partner.picture"
                  class="h-20 rounded-full border"
              /></a>

              <p class="text-center font-medium">{{ partner.name }}</p>
            </div>
          </div>

          <div class="text-gray-600"></div>
        </div>
        <div
          v-if="loading"
          class="mt-20 flex flex-col items-center justify-center md:mb-20"
          role="status"
        >
          <svg
            aria-hidden="true"
            class="h-24 w-24 animate-spin fill-red-500 text-red-100 dark:text-gray-600"
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
        <div class="-mr-2 flex items-center justify-center gap-2">
          <img
            alt="advantages"
            class="w-10"
            src="@/assets/images/advantage.svg"
          />
          <h2 class="my-20 text-2xl font-bold text-green-400">
            Наши преимущества
          </h2>
        </div>

        <div class="flex flex-col gap-8">
          <div
            class="rounded-xl bg-neutral-0 md:mx-auto md:w-3/5 md:p-7 md:shadow"
            data-aos="fade-up"
            data-aos-duration="1000"
          >
            <div class="mb-4 flex items-center justify-center gap-3">
              <img alt="" class="h-12" src="@/assets/images/team.svg" />
              <div class="text-lg">Команда экспертов</div>
            </div>
            <div class="text-gray-600">
              Мы гордимся нашей высококвалифицированной командой специалистов в
              области рекрутинга и управления персоналом. Наши эксперты обладают
              глубоким пониманием рынка труда и имеют многолетний опыт в
              успешном сопровождении клиентов.
            </div>
          </div>
          <div
            class="rounded-xl bg-neutral-0 md:mx-auto md:w-3/5 md:p-7 md:shadow"
            data-aos="fade-up"
            data-aos-duration="1000"
          >
            <div class="mb-4 flex items-center justify-center gap-3">
              <img alt="" class="h-12" src="@/assets/images/individual.svg" />
              <div class="text-lg">Индивидуальный подход</div>
            </div>
            <div class="text-gray-600" data-aos="fade-down">
              Мы понимаем, что каждая компания уникальна, и поэтому наш подход к
              решению задач клиентов всегда индивидуален. Мы тщательно
              анализируем потребности и цели каждого клиента, чтобы предложить
              наилучшие стратегии управления персоналом.
            </div>
          </div>
          <div
            class="rounded-xl bg-neutral-0 md:mx-auto md:w-3/5 md:p-7 md:shadow"
            data-aos="fade-up"
            data-aos-duration="1000"
          >
            <div class="mb-4 flex flex-wrap items-center justify-center gap-3">
              <img alt="" class="h-12" src="@/assets/images/client.svg" />
              <div class="text-lg">Клиентоориентированность</div>
            </div>
            <div class="text-gray-600" data-aos="fade-down">
              Наши клиенты - наш главный приоритет. Мы строим долгосрочные
              партнерские отношения, основанные на доверии, эффективной
              коммуникации и превосходном обслуживании.
            </div>
          </div>
        </div>
        <div class="mt-14 md:mx-auto md:w-3/5">
          <div class="md:flex" data-aos="fade-up">
            <img
              alt=""
              class="float-left mr-4 w-20"
              src="@/assets/images/deal.svg"
            />
            <div class="text-gray-600">
              <p class="mb-2">
                Мы гордимся своей репутацией надежного партнера для компаний
                всех размеров и отраслей. Благодаря нашему профессионализму,
                энтузиазму и целеустремленности, мы помогаем клиентам достичь
                успеха и процветания.
              </p>
              <p class="mb-4">
                Спасибо, что посетили наш сайт. Мы с нетерпением ждем
                возможности сотрудничать с вами и помочь вам в достижении ваших
                кадровых целей!
              </p>
              С уважением, Команда Elita Work
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>