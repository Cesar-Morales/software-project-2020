<template>
    <div>
        <b-container fluid class="mt-5 container bg-dark">
            <h1 class="text-white"><b-img :src="require('../../../app/static/logos/tierra.png')" fluid alt="Fluid image" width="100px"></b-img>Ayud-AR</h1>
        </b-container>
        <b-img :src="require('../../../app/static/logos/ayudar2.jpg')" fluid alt="Fluid image" class="mt-5 d-block center-image"></b-img>
        <b-container fluid class="mt-3 p-4 container bg-secondary">
            <h3 class="text-white">Bienvenidos a Ayud-AR!</h3>
            <hr>
            <h5 class="text-white">El sitio donde encontra su centro de ayuda mas cercano</h5>
            <h5 class="text-white">o podra crear su propio centro para ayudar a quienes lo necesiten</h5>
        </b-container>
        <div class="container mt-5 mb-5">
            <div class="row">
                <b-card-group deck>
                  <b-card bg-variant="dark" text-variant="white" header="Solicitar turno" class="text-center">
                    <b-card-text><h6>Usted puede tanto entregar como recibir algun tipo de donacion segun el centro.</h6></b-card-text>
                    <hr>
                    <router-link to="/turno"><b-button variant="warning">Ir</b-button></router-link> 
                  </b-card>
    
                  <b-card bg-variant="dark" text-variant="white" header="Crear centro" class="text-center">
                    <b-card-text><h6>Usted puede solicitar la alta de un centro de ayuda y esperar la verificacion.</h6></b-card-text>
                    <hr>
                    <router-link to="/crear-centro" ><b-button variant="success">Ir</b-button></router-link>
                  </b-card>
    
                  <b-card bg-variant="dark" text-variant="white" header="Centro mas cercano" class="text-center">
                    <b-card-text><h6>Usted puede buscar el centro mas cercano y ver su ubicacion en un mapa.</h6></b-card-text>

                    <hr>
                    <router-link to="/mapas-centros"><b-button variant="info">Ir</b-button></router-link>
                  </b-card>
                  <b-card bg-variant="dark" text-variant="white" header="Estadisticas" class="text-center">
                    <b-card-text><h6>Aqui puede ver las estadisticas de los centros de ayuda existentes.</h6></b-card-text>
                    <hr>
                    <router-link to="/estadistica"><b-button variant="danger">Ir</b-button></router-link>
                  </b-card>
                </b-card-group>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'HomeApp',
}
</script>

<style>
.center-image{
  margin-left: auto;
  margin-right: auto;
  width: 60%;
}
</style>
