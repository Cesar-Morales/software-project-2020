<template>
    <div class="row map">
        <l-map
            @click="markerFunction('marker.options.title')"
            :zoom="zoom" :center="center">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker 
            :key="index"
            v-for="(centerr,index) in centers"
            :lat-lng="latLng(centerr.coordinates)">
            <l-popup class="popup-style" ref="popup">
                <div style="width: 130px" class="list-group">
                <b>Nombre:</b>{{centerr.name}}
                <br>
                <b>Direccion:</b>{{centerr.location}}
                <br>
                <b>Desde:</b>{{centerr.start_time}}
                <br>
                <b>Hasta:</b>{{centerr.final_time}}
                <br>
                <b>Telefono:</b>{{centerr.phone_number}}
                </div>
                </l-popup>
            </l-marker>
        </l-map>
        <div>
            <b-button size="lg" id="refreshButton" variant="light" v-b-toggle.sidebar-footer>Centros</b-button>
            <b-sidebar 
                id="sidebar-footer" 
                aria-label="Centros de ayuda" 
                no-header 
                backdrop
                shadow
                >
            <template #footer="{ hide }">
            <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
                <strong class="mr-auto">Ayud-AR</strong>
                <b-button size="sm" variant="light" @click="hide">Cerrar</b-button>
            </div>
            </template>
            <div class="px-3 py-2">
                <h1>Centros </h1>
                <hr>
                <b-img :src="require('../../../app/static/logos/ayudar3.jpg')" fluid thumbnail></b-img>
                <CentersList :centers="centers"/>
            </div>
            </b-sidebar>
        </div>
    </div>
</template>
<script>
import {LMap, LTileLayer,LMarker,LPopup } from 'vue2-leaflet';
import CentersList from '../components/CentersList.vue'

export default {
    name:"Map",
    props:{centers: Array},
    data:function() {
        return {
            zoom:13,
            centers: [],
            center: L.latLng(-34.6083,-58.3712),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(-34.6083,-58.3712),
            
  }    
},
    components: { LMap, LTileLayer, LMarker, LPopup, CentersList, Map },
    methods:{
        latLng: function(coordinates){
            var splitted = coordinates.split(",");
            var lat = splitted[0];
            var lng = splitted[1];
            return L.latLng(lat,lng);
        },
        markerFunction: function(string) {
           var vm = this;
            console.log(vm.map)
         },   
    }
}
</script>
<style scoped>
    .map{
        height: 95vh;
    }
    #refreshButton {
      position: absolute;
      top: 20px;
      right: 20px;
      padding: 10px;
      z-index: 400;
    }
</style>