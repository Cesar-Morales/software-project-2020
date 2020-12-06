import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueMask from 'v-mask'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


import App from './App.vue'
import router from "./router";


Vue.use(VueMask)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
