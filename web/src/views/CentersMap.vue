<template>
    <div class="row">
        <div class="col-6">
            <CentersList :centers="centers" :onUpdate="onUpdate"/>
        </div>
        <div class="col-6">
            <Map :centers="centers" :zoomed="zoomed" :center="center"/>
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
            zoomed: 1,
            centers: [],
            lat: "-36.6083",
            lng: "-58.3712"

        }
    },
    methods:{ 
        onUpdate(lat,lng){ 
            this.zoomed = 8;
            this.lat = lat;
            this.lng = lng ;
            this.center = L.latLng(this.lat,this.lng)
        } 
    },
    created: function(){
        this.center = L.latLng(this.lat,this.lng)
        axios
            .get('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros')
            .then((r)=>{this.centers = r.data.centros})
    }
}
</script>
