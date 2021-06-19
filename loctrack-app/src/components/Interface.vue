

<template>
    <div id="interface">

        <div class="cell cell-map">
            <map-container  :dateProp="this.dates"/> 
        </div>
        <div class="cell cell-edit">
            <controls @dates="newDates"/>
        </div>
        <div class="cell cell-inspect">
            Inspect

        </div>
	
    </div>
</template>



<script>
 import  MapContainer  from './MapContainer.vue'
 import  Controls  from './Controls.vue'

 export default {
     name: 'Interface',
     components: {
         MapContainer,
         Controls,
     },
     
     data: function() {
         return {
             dates: [] ,
         };
     },
     methods: {
         newDates: function (d) {
             this.dates = d;
   

         },
     }
 }
</script>

<style>
 html, body {
     height: 100%;
     margin: 0;
 }

 #interface {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     height: 100%;
     display: grid;
     grid-template-columns: 100vh;
     grid-auto-rows: 1fr;
     grid-gap: 1rem;
     padding: 1rem;
     box-sizing: border-box;
     
 }

 .cell {
     border-radius: 4px;
     background-color: lightgrey;
 }

 .cell-map {
     grid-column: 1;
     grid-row-start: 1;
     grid-row-end: 3;
 }

 .cell-edit {
     grid-column: 2;
     grid-row: 1;
 }

 .cell-inspect {
     grid-column: 2;
     grid-row: 2;
 }
</style>
