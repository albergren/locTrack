<template>

  <div>

        <p>From:</p>
          <input type="date" v-model="fromDate">
        <p>To:</p>
        <input type="date" v-model="toDate">

        <button v-on:click="getDate">Go</button>
   
    <p>Opacity</p>
    <div>
  <input type="range" min="1" max="10" value="5" class="slider" id="opacityRange" ref="sliderValue"  v-on:change="changeOpacity()">
    </div>
    <p>Locations</p>
    <div>

    <ul>
    <li v-for="location in locations" :key="location.fields.name">
    {{ location.fields.name}}
</li>
    </ul>
    </div>
  </div>
</template>
    
<script>
import EventBus from '../event-bus';
import axios from 'axios';

export default {
    name: 'Options',
    data: function() {
        return {
            fromDate: '',
            toDate: '',
            locations: [],
        };
    },

    mounted() {
	this.getAllLocations();
	
    },
    methods: {
        changeOpacity: function () {
            EventBus.$emit('opacity', this.$refs.sliderValue.value / 10);
        },
        getDate: function () {
            EventBus.$emit('dates', [this.fromDate,this.toDate]);
        },
        getAllLocations: function () {
            
            axios.get( 'http://localhost:8000/mapVisual/get-all-locations/'
                     ).then(resp =>  {
                         let data = JSON.parse(resp.data)
                         this.locations = data;
                     }).catch(function() {
                         console.log('Failure!');
                     })
        },

    },

}
</script>

<style>

</style>

