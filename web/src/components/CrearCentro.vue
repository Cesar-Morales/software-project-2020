<template>
  <div class="crear-centro">
    <b-jumbotron class="container">
      <h3 class="text-center">Crear Centro</h3>
      <div class="row">
        <div class="col-md-6 col-12 mt-2">El nombre es: {{ nombre }}
          <b-form-input v-model="nombre" placeholder="Centro Ejemplo"></b-form-input>
          <p v-if="check_errors_for_key('nombre')">{{ print_error_key('nombre') }}</p>
        </div>

        <div class="col-md-6 col-12 mt-2"> La direccion es: {{ direccion }} 
          <b-form-input v-model="direccion" placeholder="Avenida Siempre Vivas Nro 743"></b-form-input>
          <p v-if="check_errors_for_key('direccion')">{{ print_error_key('direccion') }}</p>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El telefono es: {{ telefono }} 
          <b-form-input v-model="telefono" placeholder="11-9999-9999" type="text" v-mask="'##-####-####'"></b-form-input>
          <p v-if="check_errors_for_key('telefono')">{{ print_error_key('telefono') }}</p>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> La hora de apertura es: {{ hora_apertura }}    
          <b-form-input v-model="hora_apertura" type="time"></b-form-input>
           <p v-if="check_errors_for_key('hora_apertura')">{{ print_error_key('hora_apertura') }}</p>
        </div>

        <div class="col-md-6 col-12 mt-2"> La hora de cierre es: {{ hora_cierre }}    
          <b-form-input v-model="hora_cierre" type="time"></b-form-input>
          <p v-if="check_errors_for_key('hora_cierre')">{{ print_error_key('hora_cierre') }}</p>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El tipo de centro es: {{ tipo }}
          <b-form-input placeholder="Merendero" v-model="tipo"></b-form-input>
          <p v-if="check_errors_for_key('tipo')">{{ print_error_key('tipo') }}</p>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> La web es: {{ web }} 
          <b-form-input v-model="web" placeholder="http://www.centroejemplo.org.ar" type="url"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El email es: {{ email }} 
        <b-form-input v-model="email" placeholder="comedorejemplo@mail.com" type="email"></b-form-input>
        </div>
      </div>
        <b-alert class="mt-4" v-if="respuesta" variant="success" show>Petición creada exitosamente, espere pacientemente a que su solicitud sea aprobada.</b-alert>
        
        <div style="text-align: center;">
          <vue-recaptcha style="display: inline-block;"
            @verify='establecer_captcha'
            @expired='resetear_captcha'
            sitekey="6LfwIuwZAAAAAOJrxBMi5Er5IqvcXnPUjfdS1O2U" 
            :loadRecaptchaScript="true">
          </vue-recaptcha>
        </div>
        <div class="text-center">
          <b-button class="mt-3 btn btn-dark" :disabled="!captcha" v-on:click="crear_centro" v-b-tooltip.hover title="Confirma reCAPTCHA">
            Enviar
          </b-button>
        </div>
    </b-jumbotron>
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
      errors: "",
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
