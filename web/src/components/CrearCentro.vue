<template>
  <div>
    <p> El nombre es: {{ nombre }} </p>
    <input v-model="nombre">
    <p v-if="check_errors_for_key('nombre')">{{ print_error_key('nombre') }}</p>

    <p> La direccion es: {{ direccion }} </p>
    <input v-model="direccion">
    <p v-if="check_errors_for_key('direccion')">{{ print_error_key('direccion') }}</p>
    
    <p> El telefono es: {{ telefono }} </p>
    <input v-model="telefono">
    <p v-if="check_errors_for_key('telefono')">{{ print_error_key('telefono') }}</p>

    <p> La hora de apertura es: {{ hora_apertura }} </p>    
    <input v-model="hora_apertura" type="time">
    <p v-if="check_errors_for_key('hora_apertura')">{{ print_error_key('hora_apertura') }}</p>

    <p> La hora de cierre es: {{ hora_cierre }} </p>   
    <input v-model="hora_cierre" type="time">
    <p v-if="check_errors_for_key('hora_cierre')">{{ print_error_key('hora_cierre') }}</p>

    <p> El tipo de centro es: {{ tipo }} </p>
    <input v-model="tipo">
    <p v-if="check_errors_for_key('tipo')">{{ print_error_key('tipo') }}</p>
    
    <p> La web es: {{ web }} </p>
    <input v-model="web">
    
    <p> El email es: {{ email }} </p>
    <input v-model="email">

    <p v-if="respuesta">Petición creada exitosamente, espere pacientemente a que su solicitud sea aprobada.</p>
    <p> {{ respuesta }} </p>

    <h3>Errors</h3>
    <ul v-if="errors">
      <li v-for="error in errors" :key="error">
        {{ error[0] }}
      </li>
    </ul>

    <vue-recaptcha  
      @verify='establecer_captcha'
      @expired='resetear_captcha'
      sitekey="6LfwIuwZAAAAAOJrxBMi5Er5IqvcXnPUjfdS1O2U" 
      :loadRecaptchaScript="true"
    ></vue-recaptcha>

    <!-- AGREGAR UN MENSAJE PARA CUANDO ESTA DESHABILITADO -->
    <button  v-on:click="crear_centro"> Enviar </button>

  </div>
</template>

<script>
import axios from 'axios'
import VueRecaptcha from 'vue-recaptcha'
import qs from 'qs'

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
    check_errors_for_key(key) {
      return this.errors && this.error_contains_key(this.errors, key)
    },
    print_error_key(key) {
      return this.errors[key][0]
    },
    error_contains_key(errors, key) {
      return Object.keys(errors).includes(key)
    },
    resetear_captcha() {
      this.captcha = ""
    },
    establecer_captcha(response) {
      this.captcha = response
    },
    crear_centro() {
      axios
        .post('http://127.0.0.1:5000/centros', qs.stringify({
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
