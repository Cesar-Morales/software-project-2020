<template>
  <div id="app">
    <router-view></router-view>
    <NavBar/>
    <CrearCentro/>
    <Footer/>
  </div>
</template>

<script>
import CrearCentro from './components/CrearCentro.vue'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    CrearCentro,
    Footer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
