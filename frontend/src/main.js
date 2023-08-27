import "./assets/main.css";
import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router/index.js";
import "aos/dist/aos.css";
import Vue3Sanitize from "vue-3-sanitize";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(Vue3Sanitize);

app.mount("#app");
