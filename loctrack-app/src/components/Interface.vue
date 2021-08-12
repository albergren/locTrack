

<template>
    <div id="interface">

        <div class=" cell-map">
    <map-container /> 
        </div>
        <div class=" cell-edit">
            <options/>

        </div>
        
    </div>
</template>



<script>
 import  MapContainer  from './MapContainer.vue'
 import Options from './Options.vue'

 export default {
     name: 'Interface',
     components: {
         MapContainer,
         Options,
     },
     
     data: function() {
         return {
         };
     },
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


 .cell-map {
     grid-column: 1;
     grid-row-start: 1;
     grid-row-end: 3;
          border-radius: 4px;
     background-color: lightgrey
 }

 .cell-edit {
     grid-column: 2;
     grid-row: 1;

      border-radius: 4px;
     background-color: lightgrey;}

 .cell-options {
     grid-column: 2;
     grid-row: 2;
          border-radius: 4px;
     background-color: lightgrey;
 }
</style>
