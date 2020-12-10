import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueMask from 'v-mask'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import router from './router'
import store from './store'
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'
import './scss/main.scss'
import ECharts from 'vue-echarts'

// import ECharts modules manually to reduce bundle size
import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'

delete L.Icon.Default.prototype._getIconUrl

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png')
})
Vue.config.productionTip = false
Vue.component('v-chart', ECharts)
Vue.use(VueMask)
Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
