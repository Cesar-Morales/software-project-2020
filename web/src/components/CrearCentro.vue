<template>
  <div>
    <b-jumbotron class="container">
      <h3 class="text-center">Crear Centro</h3>
      <div class="row">
        <div class="col-md-6 col-12 mt-2">El nombre es: {{ nombre }}
          <b-form-input v-model="nombre" placeholder="Centro Tururu"></b-form-input>
        </div>

        <div class="col-md-6 col-12 mt-2"> La direccion es: {{ direccion }} 
          <b-form-input v-model="direccion" placeholder="Avenida Siempre Vivas Nro 743"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El telefono es: {{ telefono }} 
          <b-form-input v-model="telefono" placeholder="221-5552222" type="tel"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> La hora de apertura es: {{ hora_apertura }}    
          <b-form-input v-model="hora_apertura" type="time"></b-form-input>
        </div>

        <div class="col-md-6 col-12 mt-2"> La hora de cierre es: {{ hora_cierre }}    
          <b-form-input v-model="hora_cierre" type="time"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El tipo de centro es: {{ tipo }}
          <b-form-input placeholder="Comedor" v-model="tipo"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> La web es: {{ web }} 
          <b-form-input v-model="web" placeholder="http://www.centrotururu.org.ar" type="url"></b-form-input>
        </div>
        
        <div class="col-md-6 col-12 mt-2"> El email es: {{ email }} 
        <b-form-input v-model="email" placeholder="comedortururu@mail.com" type="email"></b-form-input>
        </div>
      </div>
        <p v-if="respuesta">Petición creada exitosamente, espere pacientemente a que su solicitud sea aprobada.</p>
        <p> {{ respuesta }} </p>

        <h3>Errors</h3>
        <p> {{ errors }} </p>

        <vue-recaptcha 
          @verify='establecer_captcha'
          @expired='resetear_captcha'
          sitekey="6LfwIuwZAAAAAOJrxBMi5Er5IqvcXnPUjfdS1O2U" 
          :loadRecaptchaScript="true">
        </vue-recaptcha>
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
                           this.respuesta = response.data.atributos})
        .catch(
          error => {this.respuesta = ""
                    this.errors = error.response})
    }
  }
}
</script>
