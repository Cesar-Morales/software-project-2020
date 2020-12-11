<template>
    <div>
        <Pie v-if="centros.length" :centros='centros'></Pie>
        <Histogram v-if="centros.length" :centros='centros'></Histogram>
        <Heatmap v-if="centros.length" :centros='centros'></Heatmap>
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