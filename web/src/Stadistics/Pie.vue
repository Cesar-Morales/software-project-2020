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
    props: {
        centros: Array
    },
    data() {
        return {
            paginas_web: {
                tiene: 0,
                no_tiene: 0
            },
            chartData: {
                columns: ['web', 'cantidad'],
                rows: []
            }
        }
    },
    methods: {
        contarPaginasWeb(centros) {
            for(var key of centros.keys()){
                if(centros[key].web == "" ){
                    this.paginas_web.no_tiene++
                }
                else{
                    this.paginas_web.tiene++
                }
            }
            this.chartData.rows.push({ 'web': 'Tiene web', 'cantidad': this.paginas_web.tiene})
            this.chartData.rows.push({ 'web': 'No tiene web', 'cantidad': this.paginas_web.no_tiene})
        }
    },
    mounted: function() {
        this.contarPaginasWeb(this.centros)
    }
}
</script>