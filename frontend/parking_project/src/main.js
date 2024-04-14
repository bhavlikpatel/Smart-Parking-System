import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import vuetify from "./plugins/vuetify";
import axiosInstance from "@/plugins/axios.js";
import api from "@/plugins/api.js";
import colors from "@/assets/colors.js";
import VueBarcode from "@chenfengyuan/vue-barcode";

import routes from "@/router/auth.js";
export const bus = new Vue();

Vue.config.productionTip = false;
Vue.prototype.$axios = axiosInstance;
Vue.prototype.$api = api;
Vue.prototype.$colors = colors;
Vue.component("VueBarcode", VueBarcode);

Vue.use(VueRouter);
const router = new VueRouter({
  mode: "hash",
  routes: routes,
});

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
