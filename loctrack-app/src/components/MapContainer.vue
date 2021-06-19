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
         
         plotDate: function (dates) {

             this.geojsonLayer.clearLayers();
             this.geojsonLayer.setStyle( {fillColor :'red'});

             const daysDiff = this.getDaysDiff(dates[0],dates[1]);
             

             let formattedDate = "";
             let date =  new Date(dates[0]);
             
             for (let i = 0; i < daysDiff; i++) {
                 console.log(date);
                 formattedDate = date.toISOString().split('T')[0].split("-").join("");
                 console.log(formattedDate.split("-").join(""));
                 date.setDate(date.getDate() + 1);

                 (async () => {

                     let data = await this.getData(formattedDate)
                                          .then(res => res)
                                          .catch(err => {console.log(err)});


                     let pointLayer = L.geoJSON(null, {
                         pointToLayer: function(feature,latlng){
                             console.log(feature);
                             const label = String(feature.properties.name)
                             return new L.CircleMarker(latlng, {
                                 radius: 1,
                             }).bindTooltip(label, {permanent: true, opacity: 0.7}).openTooltip();
                     }});
                     pointLayer.addData(data)
                     //this.geojsonLayer.addLayer(pointLayer);

                     
                     this.geojsonLayer.addData(data)
                 }
                 )();
             }
         },
         
         getDaysDiff: function (date1, date2) {
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
