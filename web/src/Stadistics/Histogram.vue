<template>
  <ve-histogram class="mb-1" :data="chartData"></ve-histogram>
</template>

<script>
  import VeHistogram from 'v-charts/lib/histogram.common'
  export default {
    name: 'Histogram',
    components: {
        VeHistogram
    },
    props: {
      centros: Array
    },
    data () {
      return {
        tiposCentros: {},
        chartData: {
          columns: ['tipo', 'Cantidad'],
          rows: []
        }
      }
    },
    methods: {
        contarTiposCentros(centros) {

          //Obtener y contar los tipos de centros
                for(var key of centros.keys()){
                    if(centros[key].tipo in this.tiposCentros ){
                        this.tiposCentros[centros[key].tipo]++
                    }
                    else{
                        this.tiposCentros[centros[key].tipo] = 1
                    }
          }
          
          //Poner los datos en charData
          for(var tipo of Object.keys(this.tiposCentros)){
              this.chartData.rows.push({tipo: tipo, 'Cantidad': this.tiposCentros[tipo]})
          }
        }
    },
    mounted: function() {
        this.contarTiposCentros(this.centros)
    }
  }
</script>