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
                <div class="list-group">
                    {{centerr.name}}<br> {{centerr.location}}<br> {{centerr.start_time}}<br> {{centerr.final_time}}<br> {{centerr.phone_number}}
                </div>
                </l-popup>
            </l-marker>
      </l-map>
    </div>
</template>
<script>
import {LMap, LTileLayer,LMarker,LPopup } from 'vue2-leaflet';


export default {
    name:"Map",
    props:{centers: Array},
    data:function() {
        return {
            zoom:13,
            center: L.latLng(-34.6083,-58.3712),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(-34.6083,-58.3712),
            
  }    
},
    components: { LMap, LTileLayer, LMarker, LPopup },
   
    methods:{
        latLng: function(coordinates){
            var splitted = coordinates.split(",");
            var lat = splitted[0];
            var lng = splitted[1];
            return L.latLng(lat,lng);
        },
    }

}
</script>
<style scoped>
    .map{
        height: 95vh;
    }
</style>