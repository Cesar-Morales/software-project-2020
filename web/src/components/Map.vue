<template>
    <div class="row map">
      <l-map
        :center="center"
        :zoom="zoomed">

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
import { LMap, LTileLayer, LMarker, LPopup } from 'vue2-leaflet';
export default {
    name:"Map",
    components: { 
        LMap, 
        LTileLayer, 
        LMarker, 
        LPopup
    },
    props:{
        centers: Array, 
        zoomed: Number, 
        center: Object,
        set_zoom: Function
        },
    data:function() {
        return {
            zoom: null,
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        }    
    },
    methods: {
        latLng: function(coordinates){
            var splitted = coordinates.split(",")
            var lat = splitted[0]
            var lng = splitted[1]
            return L.latLng(lat,lng)
        },
        
    },
    mounted: function () {
        console.log(this.$children)
    }
}
</script>


<style scoped>
    .map{
        height: 95vh
    }
</style>