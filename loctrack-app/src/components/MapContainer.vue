<template>
    <div id="map" style="height: 100%; width: 100%"/>
</template>

<script>
import L from 'leaflet';

 export default {
     name: "MapContainer",
     components: {
         //LMap,
         //LTileLayer,
     },
     props: {
         dateProp: Array
     },
     
     data() {
         return {
             url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
             zoom: 9,
             center: [55.18, 12.0],
             geojsonLayer: "",
         }
     },
     
     watch: {
         dateProp: function(newDates) {
             this.plotDate(newDates);
         }
     },
     
     methods: {
         getData: async (date) => {
             let response = await fetch('http://localhost:8000/mapVisual/' + date);
             let data = await response.json();
             return data;
         },
         getData2: async (date1, date2) => {
             let url = new URL('http://localhost:8000/mapVisual/get-trackpoints');
             url.search = new URLSearchParams( {start: date1, end: date2 });
             let response = await fetch(url);
             let data = await response.json();
             console.log(data);
             return data;
         },
         plotDate: function (dates) {
             this.geojsonLayer.clearLayers();

             const daysDiff = this.calcDaysDiff(dates[0],dates[1]);
             

             let date =  new Date(dates[0]);
             //let date2 = new Date(dates[1]);
             console.log("");
             for (let i = 0; i < daysDiff; i++) {
                 let formattedDate1 = date.toISOString()
                 let date2 = new Date(date.setDate(date.getDate() + 1));
                 console.log(date2);
                 let formattedDate2 = date2.toISOString();

 
                 (async () => {

                     let data = await this.getData2(formattedDate1, formattedDate2)
                                         .then(res => res)
                                         .catch(err => {console.log(err)});

                     console.log("lkj");
                     console.log(data);
                     console.log("sldkjfsdlkfj");
                     let pointLayer = L.geoJSON(JSON.parse(data), {
                         pointToLayer: function(feature,latlng){
                             let marker = new L.circle(latlng,0.01);
                             return marker;
                     }});
                     //pointLayer.addData(data)
                     console.log("lksdjfsdj");
                     this.geojsonLayer.addLayer(pointLayer);



                     //this.geojsonLayer.addData(data)
                     
                 }
                 )();
             }
         },

         // Calculate number of days between two dates
         calcaysDiff: function (date1, date2) {
             const _MS_PER_DAY = 1000 * 60 * 60 * 24;
             const a = new Date(date1);
             const b = new Date(date2);
             const utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
             const utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());
             const daysDiff =  (date2 != "") ? Math.floor((utc2 - utc1) / _MS_PER_DAY) : 1;
             return daysDiff;
         },
     },
     
     mounted() {
         
         let mymap =  L.map('map').setView(this.center, this.zoom);
         L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
             maxZoom: 19,
             attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
         }).addTo(mymap);

         function polystyle() {
             return {
                 fillColor: 'blue',
                 weight: 2,
                 opacity: 1,
                 color: 'green',  //Outline color
                 fillOpacity: 0.7
             };
         }

         this.geojsonLayer = L.geoJSON("", {style: polystyle}).addTo(mymap);

     },
 }
</script>
