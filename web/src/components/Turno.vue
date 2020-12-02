<template>
	<div class='turno'>
		<h1> Solicitar Turno</h1>
		<form @submit.prevent="onSubmit">
			<label for="email">Email:</label>
			<input v-model="email_donante" id="email">
			<label for="telefono">Telefono:</label>
			<input v-model="telefono_donante" id="telefono">
			<label for="centro">Centro:</label>
			<select v-model="centro_id" id="centro" @change="solicitarTurnos()">
				<option v-for="centro in centros" :value="centro.id" :key="centro.id">{{centro.name}}</option>
			</select>
			<label for="fecha" v-if="centro_id">Fecha:</label>
			<input type="date" id="fecha" v-model="fecha" @change="solicitarTurnos()" v-if="centro_id">
			<label for="turno">Horario: </label>
			<select v-model="turno" id="turno">
				<option v-for="turno in turnos" v-bind:value="turno" v-bind:key="turno">{{turno.hora_inicio}}</option>
			</select>
			<button class="btn btn-lg btn-primary pull-xs-right">
              Solicitar
            </button>
		</form>
		<p> {{ errors }}</p>
	</div>
</template>
<script>
	import axios from 'axios'
	import qs from 'qs'
	export default {
		name: 'Turno',
		components: {
		},
		data() {
			return{
				centro_id: null,
				email_donante: "",
				telefono_donante: "",
				hora_inicio: null,
				hora_fin: null,
				turno: null,
				fecha: new Date('2020-12-04'),
				centros: [],
				errors:"",
				turnos: [],
				respuesta: "",
			}
		},
		mounted () {
            axios
            .get('http://127.0.0.1:5000/centros')
            .then(response => (this.centros = response.data.centros))
            .catch(error => this.errors = error.response)
        },
		methods: {
			onSubmit() {
				var date = new Date(this.fecha)
				axios
				.post('http://127.0.0.1:5000/centros/'.concat(this.centro_id).concat('/reserva'), qs.stringify({
					centro_id: this.centro_id,
					email_donante: this.email_donante,
					telefono_donante: this.telefono_donante,
					hora_inicio: this.turno.hora_inicio,
					hora_fin: this.turno.hora_fin,
					fecha: date.getFullYear() + '-' + ('0'+ (date.getMonth()+1)).slice(-2) + '-' +
                           ('0'+ (date.getDate() + 1)).slice(-2)}))
                .then(response => {this.errors = "",
                                  this.respuesta = response.data.atributos,
                                  this.turno = null})
                .catch(error => {this.errors = error.response,
                                this.respuesta = ""})
			},
            solicitarTurnos() {
                var date = new Date(this.fecha)
                axios
                .get('http://127.0.0.1:5000/centros/'.concat(this.centro_id).concat('/turnos_disponibles?fecha=').concat(date.getFullYear() + '-' + ('0'+ (date.getMonth()+1)).slice(-2) + '-' +
                ('0'+ (date.getDate() + 1)).slice(-2)))
                .then(response => (this.turnos = response.data.turnos))
                .catch(error => this.errors = error.response)
                this.turno = null;
			}
		}
	}
</script>