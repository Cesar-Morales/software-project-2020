<template>
    <div>
        <ve-pie :data="chartData"></ve-pie>
    </div>
</template>

<script>
import VePie from 'v-charts/lib/pie.common'

export default {
  name: 'Pie',
  components: {
      VePie
  },
  data() {
    return {
        chartData: {
          columns: ['web', 'cantidad'],
          rows: [
            { 'web': 'Tiene web', 'cantidad': 123},
            { 'web': 'No tiene web', 'cantidad': 1223}
          ]
        }
    }
  }
}
</script>