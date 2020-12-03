import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'



delete L.Icon.Default.prototype._getIconUrl

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png')
})
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
