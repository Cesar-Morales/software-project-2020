<template>
    <div>
        <Pie></Pie>
        <Histogram></Histogram>
    </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import Pie from './Pie.vue'
import Histogram from './Histogram.vue'

export default {
  name: 'Stadistic',
  components: {
      Pie,
      Histogram
  },
  data() {
    return {
        tipo: "",
        centers_with_web: 0,
        centers_without_web: 0,
        location: "",
        respuesta: "",
        errors: "",
    }
  },
  methods: {
    crear_centro() {
      axios
        .post('https://admin-grupo12.proyecto2020.linti.unlp.edu.ar/centros', qs.stringify({
          nombre: this.nombre,
          direccion: this.direccion,
          telefono: this.telefono,
          hora_apertura: this.hora_apertura,
          hora_cierre: this.hora_cierre,
          tipo: this.tipo,
          web: this.web,
          email: this.email}))
        .then(response => {this.errors = ""
                           this.respuesta = response.data})
        .catch(
          error => {this.respuesta = ""
                    this.errors = error.response.data.error_message})
    }
  }
}
</script>