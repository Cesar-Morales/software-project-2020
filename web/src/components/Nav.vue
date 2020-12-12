<template>
  <div class="hello" style="min-height: 1000px">
    <div class="link">
        <b-nav class="bg-dark" tabs align="center">
          <b-nav-item to="/" exact exact-active-class="active" class="text-white">Ayud-AR </b-nav-item>
          <b-nav-item to="/turno" class="text-white" exact exact-active-class="active">Solicitar Turno</b-nav-item>
          <b-nav-item to="/crear-centro" class="text-white" exact exact-active-class="active">Crear Centros</b-nav-item>
          <b-nav-item to="/mapas-centros" class="text-white" exact exact-active-class="active">Ubicacion de Centros</b-nav-item>
          <b-nav-item to="/estadistica" class="text-white" exact exact-active-class="active">Estadisticas</b-nav-item>
        </b-nav>
        <router-view ></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
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
  color: #FFF;
  }
a:link {
  text-decoration: none!important
  }
a:visited {
  color: white; font-family: arial; 
  text-decoration: none;
  }

</style>
