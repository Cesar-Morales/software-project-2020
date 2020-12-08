<template>
    <div class="row">
        <div class="col-6">
            <CentersList :centers="centers" :onUpdate="onUpdate"/>
        </div>
        <div class="col-6">
            <Map :centers="centers" :zoomed="zoomed" :center="center" :set_zoom="set_zoom" />
        </div>
    </div>


 
</template>


<script>
import CentersList from '../components/CentersList.vue'
import axios from 'axios'
import Map from '../components/Map.vue'

export default {
    name: 'CenterList',
    components:{CentersList,Map},
    data:function(){
        return {
            center:null,
            zoomed: 4,
            centers: [],
            lat: "-38.416097",
            lng: "-63.616672",
            map: null

        }
    },
    methods:{ 
        onUpdate(lat,lng){
            console.log(this.map.zoom)
            this.lat = lat
            this.lng = lng
            this.map.flyTo([this.lat, this.lng], 15)
        },
        sleep(milliseconds) {
            var start = new Date().getTime()
            for (var i = 0; i < 1e7; i++) {
                if ((new Date().getTime() - start) > milliseconds) {
                    break;
                }
            }
        },
        set_zoom: function(){
            this.zoomed = 8
        }
    },
    created: function(){
        this.center = L.latLng(this.lat,this.lng)
        axios
            .get('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros')
            .then((r)=>{this.centers = r.data.centros})
    },
    mounted: function(){
        this.map = this.$children[1].$children[0].mapObject
    }
}
</script>
