<template>
    <div class="row">
        <div class="col-6">
            <CentersList :centers="centers" :onUpdate="onUpdate"/>
        </div>
        <div class="col-6">
            <Map :centers="centers" :zoom="zoom" :lat="lat" :lng="lng"/>
        </div>
    </div>


 
</template>


<script>
import CentersList from '../components/CentersList.vue'
import axios from 'axios'
import Map from '../components/Map.vue'
import {LMarker } from 'vue2-leaflet';

export default {
  name: 'CenterList',
  components:{CentersList,Map},
  data:function(){
      return {
          center:null,
          zoom:13,
          centers: [],
          lat:"-34.6083",
          lng:"-58.3712"

      }
  },
  mounted: function(){
      axios.get('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros').then((r)=>{this.centers = r.data.centros;console.log(this.centers)
      });
     
  },
  methods:{ 
    onUpdate(lat,lng){
    console.log(lat); 
    console.log(lng);  
    this.zoom=15;
    this.lat = lat;
    this.lng = lng ;
      } 
    }
   
  }

</script>
