<template>
    <div class="container">
        <b-container fluid class="bg-dark pt-1 pb-1 pl-4 pr-4 mt-5 mb-5">
        <div class="row mt-5">
            <div class="col-5">
              <b-card style="max-width: 25rem;" header-bg-variant="info" header-tag="header" footer-tag="footer">
                <template #header>
                  <h6 class="mb-0 text-white">Centros con Paginas Web</h6>
                </template>
                <b-card-text>
                   <Pie class="center-text mt-2" v-if="centros.length" :centros='centros'></Pie>
                </b-card-text>
              </b-card>
            </div>        
            <div class="col-7">
              <b-card
                header="Tipos de Centros"
                header-text-variant="white"
                header-tag="header"
                header-bg-variant="info"
                style="max-width: 40rem;">
                <b-card-text>
                    <Histogram v-if="centros.length" :centros='centros'></Histogram>
                </b-card-text>
              </b-card>
            </div>
        </div>
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8 mt-5 mb-5">
                <b-card
                  header="Tipo de Centro por Provincia"
                  header-text-variant="white"
                  header-tag="header"
                  header-bg-variant="info"
                  style="max-width: 50rem;">
                  <b-card-text>
                      <Heatmap v-if="centros.length" :centros='centros'></Heatmap>
                  </b-card-text>
                </b-card>
            </div>
            <div class="col-2"></div> 
        </div>    
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'
import Pie from '../Stadistics/Pie'
import Histogram from '../Stadistics/Histogram'
import Heatmap from '../Stadistics/Heatmap'
import Map from '../Stadistics/Map'

export default {
    name: 'Stadistic',
    components: {
        Pie,
        Histogram,
        Heatmap,
        Map
    },
    data() {
        return {
            centros: []
        }
    },
     watch: {
        centros: function (value) {
            this.centros = value
        }
    },
    mounted: function() {
        axios
        .get('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros')
        .then(response => {this.centros = response.data.centros})
    }
}
</script>