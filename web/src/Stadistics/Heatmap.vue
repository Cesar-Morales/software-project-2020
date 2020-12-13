<template>
  <v-chart :options="heatmap"/>
</template>

<script>
import axios from 'axios'
import ECharts from 'vue-echarts'
import 'echarts/lib/chart/heatmap'
import 'echarts/lib/component/visualMap'

export default {
    name: 'Heatmap',
    components: {
        'v-chart': ECharts
    },
    props:{
        centros: Array
    },
    data () {
        //Este está bien que este hecho manualmente
        var provincias = ['Jujuy', 'Salta', 'Formosa', 
                    'Corrientes', 'Misiones', 'Entre Rios', 
                    'Chaco', 'San Luis', 'Catamarca',
                    'Mendoza', 'La Pampa', 'Buenos Aires',
                    'Chubut', 'Rio Negro', 'Santiago del Estero',
                    'Cordoba', 'Tucuman', 'San Juan',
                    'La Rioja', 'Santa Fe', 'Neuquen',
                    'Chubut', 'Santa Cruz', 'Tierra del Fuego'
                    ]

        return {
            tiposCentros: {},
            tipos: [],
            actualKey: undefined,
            provinciaActual: undefined,
            heatmapData: {},
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
                    data: this.tipos
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
                    data: [],
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
    },
    methods: {
        async actualizarData(p) {

            if(p != undefined){
                if(p in this.heatmapData){
                    if(this.centros[this.actualKey].tipo in this.heatmapData[p]){
                        this.heatmapData[p][this.centros[this.actualKey].tipo]++
                    }
                    else{
                        this.heatmapData[p][this.centros[this.actualKey].tipo] = 1
                    }
                }
                else{
                    this.heatmapData[p] = {}
                    this.heatmapData[p][this.centros[this.actualKey].tipo] = 1
                }
            }
        },
        obtenerProvincia(coordinates){
            var splitted = coordinates.split(",")
            var lat = splitted[0]
            var lng = splitted[1]

            return axios.get('https://apis.datos.gob.ar/georef/api/ubicacion?lat=' + lat + '&lon=' + lng)

        },
        async obtenerData(centros) {

            var response

			//Obtener y contar los tipos de centros
            for(var key of centros.keys()){
                this.actualKey = key
                console.log(centros[key].coordinates)
                if(centros[key].coordinates != ""){
                    response = await this.obtenerProvincia(centros[key].coordinates)
                    await this.actualizarData(response.data.ubicacion.provincia.nombre)
                }
            }

            console.log(this.heatmap.series[0].data)

            //Poner los datos en charData
            for(var provincia of Object.keys(this.heatmapData)){
                for(var tipo of Object.keys(this.heatmapData[provincia])){
                    this.heatmap.series[0].data.push([provincia, tipo, this.heatmapData[provincia][tipo]])
                }
            }
        },
        obtenerTiposCentros(centros) {

            //Obtener y contar los tipos de centros
            for(var key of centros.keys()){
                if(!(centros[key].tipo in this.tiposCentros)){
                    this.tiposCentros[centros[key].tipo] = 1
                }
            }
          
            //Poner los datos en charData
            for(var tipo of Object.keys(this.tiposCentros)){
                this.tipos.push(tipo)
            }
        }
    },
    mounted: function() {
        this.obtenerTiposCentros(this.centros)
        this.obtenerData(this.centros)
    }
}
</script>