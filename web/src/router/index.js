import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Turno from '../components/Turno.vue'
import Home from '../components/Home.vue'

export default new Router({
	routes: [
    { path: '/turno', component: Turno},
    { path: '/', component: Home}
  ]
})