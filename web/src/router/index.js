import Vue from 'vue'
import VueRouter from 'vue-router'
import CentersMap from '../views/CentersMap.vue'
import Turno from '../components/Turno.vue'
import CrearCentro from '../components/CrearCentro.vue'
Vue.use(VueRouter)

const routes = [
  {
    path:'/mapas-centros',
    name:'mapas-centros',
    component:CentersMap
  },
  { path: '/turno', component: Turno},
  { path: '/crear-centro', component: CrearCentro}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

