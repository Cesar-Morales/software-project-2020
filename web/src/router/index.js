import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import CentersMap from '../views/CentersMap.vue'
import Turno from '../components/Turno.vue'
import CrearCentro from '../components/CrearCentro.vue'
Vue.use(VueRouter)

const routes = [
  {
    path:'/CentersMap',
    name:'CentersMap',
    component:CentersMap
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
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

