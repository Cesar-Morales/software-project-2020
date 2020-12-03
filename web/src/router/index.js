import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Turno from '../components/Turno.vue'
import Home from '../components/Home.vue'
import CrearCentro from '../components/CrearCentro.vue'

var route = new Router({
  mode: 'history', 
  base: process.env.BASE_URL,
	routes: [
    { path: '/turno', component: Turno},
    { path: '/crear-centro', component: CrearCentro},
    { path: '/', component: Home}
  ]
})
export default route