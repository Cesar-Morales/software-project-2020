<template>
    <div class="row">
        <div class="col-6">
            <CentersList :centers="centers"/>
        </div>
        <div class="col-6">
            <Map :centers="centers"/>
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
      axios.get('http://localhost:5000/centros').then((r)=>{this.centers = r.data.centros;
      })
  }   
  }
</script>
