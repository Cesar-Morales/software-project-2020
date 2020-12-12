<template>
  <v-chart :options="map"/>
</template>

<script>
import ECharts from 'vue-echarts'
//El mapa tengo que seguir haciendolo
import argenMap from '../jsonMaps/ar-geo.json'
import 'echarts/lib/chart/map'
import 'echarts/lib/component/visualMap'

ECharts.registerMap('AR', argenMap)

export default {
  components: {
    'v-chart': ECharts
  },
  data () {
    return {
      map: {
        title: {
            text: 'Argentina',
            subtext: 'Centros de ayuda '
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b}<br/>{c} (Cantidad de centros)'
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {}
            }
        },
        visualMap: {
            min: 0,
            max: 1000,
            text: ['High', 'Low'],
            realtime: false,
            calculable: true,
            inRange: {
                color: ['lightskyblue', 'yellow', 'orangered']
            }
        },
        series: [
            {
                name: 'ArgenMap',
                type: 'map',
                map: 'AR',
                label: {
                    show: true
                },
                // Label con el que se muestra en el mapa y se cargan en 
                // los datos, util para estandarizar nombres.
                nameMap: {
                    'Buenos Aires': 'Buenos Aires'
                },
                data: [
                    {name: 'Buenos Aires', value: 100},
                    {name: 'La Pampa', value: 500}
                ]
            }
        ]
      }
    }
  }
}
</script>