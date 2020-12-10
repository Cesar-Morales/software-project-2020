<template>
  <ve-histogram :data="chartData" :settings="chartSettings"></ve-histogram>
</template>

<script>
  import VeHistogram from 'v-charts/lib/histogram.common'
  export default {
    name: 'Histogram',
    components: {
        VeHistogram
    },
    data () {
      return {
        chartData: {
          columns: ['tipo', 'cantidad'],
          rows: [
            { 'tipo': 'Institucion religiosa', 'cantidad': 1523},
            { 'tipo': 'Merendero', 'cantidad': 122}
          ]
        }
      }
    }
  }
</script>