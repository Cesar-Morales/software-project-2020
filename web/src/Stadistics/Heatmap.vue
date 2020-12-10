<template>
  <v-chart :options="heatmap"/>
</template>

<script>
import ECharts from 'vue-echarts'
import 'echarts/lib/chart/heatmap'
import 'echarts/lib/component/visualMap'

export default {
  name: 'Heatmap',
  components: {
    'v-chart': ECharts
  },
  data () {
    //Este está bien que este hecho manualmente
    let provincias = ['Jujuy', 'Salta', 'Formosa', 
                 'Corrientes', 'Misiones', 'Entre Rios', 
                 'Chaco', 'San Luis', 'Catamarca',
                 'Mendoza', 'La Pampa', 'Buenos Aires',
                 'Chubut', 'Rio Negro', 'Santiago del Estero',
                 'Cordoba', 'Tucuman', 'San Juan',
                 'La Rioja', 'Santa Fe', 'Neuquen',
                 'Chubut', 'Santa Cruz', 'Tierra del Fuego'
                ]

    //Este habría que llenarlo con los tipos de centros diferentes, podemos hacer una API
    //o iterar por todos los centros
    let tipos = ['Institucion religiosa', 'Merendero']

    //Aca se podría hacer la cuenta de la cantidad de cada tipo
    let data = [['Jujuy','Merendero',15],
                ['Tucuman','Institucion religiosa',5],
                ['Santa Cruz','Merendero',5]]

    return {
      heatmap: {
        tooltip: {
            position: 'top'
        },
        animation: false,
        grid: {
            height: '20%',
            width: '80%',
            top: '20%',
            left: '20%'
        },
        xAxis: {
            type: 'category',
            data: provincias,
            axisLabel: {
                interval: 0,
                rotate: 90
            }
        },
        yAxis: {
            type: 'category',
            data: tipos
        },
        visualMap: [{
            type: 'continuous',
            min: 0,
            max: 10,
            calculable: true,
            orient: 'horizontal',
            left: '50%',
            bottom: '10%'
        }],
        series: [{
            name: 'Cantidad de centros',
            type: 'heatmap',
            data: data,
            label: {
                show: true
            },
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
      }
    }
  }
}
</script>