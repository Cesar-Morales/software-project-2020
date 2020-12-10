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
      this.chartSettings = {
        axisSite: { right: ['growthRate'] },
        yAxisType: ['KMB', 'percent'],
        yAxisName: ['number', 'rate']
      }
      return {
        chartData: {
          columns: ['date', 'cost', 'profit', 'growthRate', 'people'],
          rows: [
            { 'date': '01/01', 'cost': 1523, 'profit': 1523, 'growthRate': 0.12, 'people': 100 },
            { 'date': '01/02', 'cost': 1223, 'profit': 1523, 'growthRate': 0.345, 'people': 100 },
            { 'date': '01/03', 'cost': 2123, 'profit': 1523, 'growthRate': 0.7, 'people': 100 },
            { 'date': '01/04', 'cost': 4123, 'profit': 1523, 'growthRate': 0.31, 'people': 100 }
          ]
        }
      }
    }
  }
</script>