<template>
<div class="row">
   <div class="col-6">
       </div> 
</div>

 
</template>


<script>
import CentersList from '../components/CentersList.vue'
import axios from 'axios'
export default {
  name: 'CentersList',
  components:{CentersList},
  data:function(){
      return{
          centers: []
      }
  },
  mounted: function(){
      axios.get('http://localhost:5000/centros').then((r)=>{this.centers = r.data;
      })
  }    
  }
</script>