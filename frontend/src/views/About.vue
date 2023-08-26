<script setup>
import { onMounted } from "vue";
import AOS from "aos";

onMounted(() => {
  AOS.init();
});
</script>

<template>
  <main class="min-h-screen bg-gray-100 font-sans">
    <div class="container">
      <div class="rounded-lg bg-white p-8 shadow-md">
        <h1 class="mb-7 text-center text-3xl font-semibold md:mb-14">О нас</h1>
        <div
          class="mb-6 text-gray-600 md:mx-auto md:w-3/5"
          data-aos="fade-left"
          data-aos-duration="1000"
        >
          Компания Elita Work - это инновационная и динамично развивающаяся
          организация, специализирующаяся в области трудоустройства, рекрутинга
          и управления персоналом. С нашим богатым опытом и экспертизой в сфере
          человеческих ресурсов, мы стремимся предоставлять клиентам
          высококачественные решения для эффективного управления персоналом.
        </div>
        <div
          class="md:mx-auto md:w-3/5"
          data-aos="fade-right"
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
        <div class="-mr-2 flex items-center justify-center gap-2">
          <img
            alt="advantages"
            class="w-10"
            src="@/assets/images/advantage.svg"
          />
          <h2 class="my-20 text-2xl font-bold text-green-400">
            Наши преймущества
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
            <div class="mb-4 flex items-center justify-center gap-3">
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