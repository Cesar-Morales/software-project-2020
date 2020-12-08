<template>
  <div class="hello">
    <div class="link">
      <router-link to="/turno"><b-button class="mr-1">Solicitar Turno</b-button></router-link>
      <router-link to="/crear-centro"><b-button class="ml-1">Crear Centros</b-button></router-link>
      <router-link to="/CentersMap"><b-button class="ml-1">Ver Ubicacion de Centros</b-button></router-link>
      <router-link to="/estadistica"><b-button class="ml-1">Estadisticas</b-button></router-link>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
