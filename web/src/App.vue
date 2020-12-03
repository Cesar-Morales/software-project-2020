<template>
  <div id="app">
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
