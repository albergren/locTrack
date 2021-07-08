
<template>
    <div>
     <br><br>
        <div class="large-12 medium-12 small-12 cell">
          <label>File upload
            <input type="file" id="files" ref="files" multiple v-on:change="handleFileUpload()"/>
          </label>
    <button v-on:click="submitFiles">Submit</button>
    
    </div>
    <br>
    <div >
    <button v-if="!newLocation" v-on:click="createNewLocation">New location</button>
    </div>
    <div v-if="newLocation">
    <br>
    <div class="large-12 medium-12 small-12 cell">
    <label>New location
    <input type="text" id="locationName" v-model="newLocationName" placeholder="Name"/>
    <input type="text" id="locationCategory" v-model="newLocationCategory" placeholder="Category"/>
    <input type="text" id="locationDuration" v-model="newLocationDuration" placeholder="Duration"/>
    <input type="color"  id="locationColor" v-model="newLocationColor" v-on:change="changeLocationColor"/>
    </label>
    <br>
    <button v-on:click="addNewLocation">Add</button>
        <button v-on:click="cancelNewLocation">Cancel</button>

    </div>
    </div>
    </div>
</template>



<script>
import axios from 'axios';
import EventBus from '../event-bus';

export default {
    name: 'Controls',
    methods: {
        createNewLocation: function () {
            this.newLocation = true;
            EventBus.$emit('newLoc', this.newLocation);
            EventBus.$on('locationPolygon', data => {this.newLocationPolygon = data});
        },
        cancelNewLocation: function () {
            this.newLocation = false;
            EventBus.$emit('newLoc', this.newLocation);
            EventBus.$off('locationPolygon');

        },

        addNewLocation: function () {
            this.newLocation = false;
            axios.post( 'http://localhost:8000/mapVisual/add-new-location/',
                        JSON.stringify( {
                            name: this.newLocationName,
                            category: this.newLocationCategory,
                            duration: this.newLocationDuration,
                            color: this.newLocationColor,
                            polygon: this.newLocationPolygon
                        }),
                        {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            }
                        }
                      ).then(function() {
                          console.log('Success!');
                      }).catch(function() {
                          console.log('Failure!');
                      });

        },

        changeLocationColor: function () {
            EventBus.$emit('newLocColor', this.newLocationColor);
                
        },

        handleFileUpload: function () {
            this.files = this.$refs.files.files;	    
        },
        submitFiles: function () {
            let formData = new FormData();
            for ( let i = 0; i < this.files.length; i++ ) {
                let file = this.files[i];
                formData.append(this.files[i].name, file);
            }

            axios.post( 'http://localhost:8000/mapVisual/import-data-gpx/',
                        formData,
                        {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            }
                        }
                      ).then(function() {
                          console.log('Success!');
                      }).catch(function() {
                          console.log('Failure!');
                      });
                                      
            },
    },
    data() {
      return {
          files: '',
          newLocation: false,
          newLocationColor: '#5186db',
          newLocationName: '',
          newLocationDuration: '',
          newLocationCategory: '',
          newLocationPolygon: '',
          



      }
    }

}
</script>

<style>
  
</style>
