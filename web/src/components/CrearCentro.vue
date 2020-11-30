<template>
  <div>
    <input v-model="nombre">
    <p> El nombre es: {{ nombre }} </p>
    <input v-model="direccion">
    <p> El direccion es: {{ direccion }} </p>
    <input v-model="telefono">
    <p> El telefono es: {{ telefono }} </p>
    <input v-model="hora_apertura">
    <p> El hora_apertura es: {{ hora_apertura }} </p>
    <input v-model="hora_cierre">
    <p> El hora_cierre es: {{ hora_cierre }} </p>
    <input v-model="tipo">
    <p> El tipo es: {{ tipo }} </p>
    <input v-model="web">
    <p> El web es: {{ web }} </p>
    <input v-model="email">
    <p> El email es: {{ email }} </p>

    <h3>Respeusta</h3>
    <p> {{ respuesta }} </p>

    <h3>Errors</h3>
    <p> {{ errors }} </p>

    <vue-recaptcha  
      @verify='mi_metodo' 
      sitekey="6LfwIuwZAAAAAOJrxBMi5Er5IqvcXnPUjfdS1O2U" 
      :loadRecaptchaScript="true"
    ></vue-recaptcha>

    <!-- AGREGAR UN MENSAJE PARA CUANDO ESTA DESHABILITADO -->
    <button :disabled="!captcha" v-on:click="crear_centro"> Enviar </button>

  </div>
</template>

<script>
import axios from 'axios'
import VueRecaptcha from 'vue-recaptcha'

export default {
  name: 'CrearCentro',
  components: { 
    VueRecaptcha
  },
  data() {
    return {
      nombre: "",
      direccion: "",
      telefono: "",
      hora_apertura: "",
      hora_cierre: "",
      tipo: "",
      web: "",
      email: "",
      respuesta: "",
      captcha: "",
      errors: ""
    }
  },
  methods: {
    mi_metodo(response) {
      this.captcha = response
    },
    crear_centro() {
      axios
        .post('http://127.0.0.1:5000/centros',{
          nombre: this.nombre,
          direccion: this.direccion,
          telefono: this.telefono,
          hora_apertura: this.hora_apertura,
          hora_cierre: this.hora_cierre,
          tipo: this.tipo,
          web: this.web,
          email: this.email})
        .then(response => {this.errors = ""
                           this.respuesta = response.data.atributos})
        .catch(
          error => {this.respuesta = ""
                    this.errors = error.response})
    }
  }
}
</script>
