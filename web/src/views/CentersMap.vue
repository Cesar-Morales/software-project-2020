<template>
    <div class="container">    
        <div class="row">
            <div class="col-12">
                <Map :centers="centers"/>
            </div>
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
          centers: []
      }
  },
  mounted: function(){
      axios.get('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros').then((r)=>{this.centers = r.data.centros;console.log(this.centers)
      })
  }   
  }
</script>
