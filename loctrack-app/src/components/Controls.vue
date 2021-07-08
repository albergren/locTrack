
<template>
    <div>

        <p>From:</p>
          <input type="date" v-model="fromDate">
        <p>To:</p>
        <input type="date" v-model="toDate">

        <button v-on:click="getDate">Go</button>
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
    <input type="text" id="locationName" placeholder="Name"/>
    <input type="text" id="locationCategory" placeholder="Category"/>
    <input type="text" id="locationDuration" placeholder="Duration"/>
    <input type="color" id="locationColor" v-model="newColor" v-on:change="changeLocationColor"/>
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
        },
        cancelNewLocation: function () {
            this.newLocation = false;

        },

        addNewLocation: function () {
            this.newLocation = false;
            this.$emit('newLoc', this.newLocation);
        },

        changeLocationColor: function () {
            EventBus.$emit('newLocColor', this.newColor);
                
        },
        getDate: function () {
            this.$emit('dates', [this.fromDate,this.toDate]);
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
          fromDate: '',
          toDate: '',
          files: '',
          newLocation: false,
          newColor: '',
      }
    }

}
</script>

<style>
  
</style>
