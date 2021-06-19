
<template>
<div>
  <p>From:</p>
  <input type="date" v-model="fromDate">
  <p>To:</p>
  <input type="date" v-model="toDate">

  <button v-on:click="getDate">Go</button>

  <div class="large-12 medium-12 small-12 cell">
      <label>File upload
        <input type="file" id="files" ref="files" multiple v-on:change="handleFileUpload()"/>
      </label>
        <button v-on:click="submitFiles()">Submit</button>
  </div>
</div>
</template>



<script>
import axios from 'axios';
  
export default {
    name: 'Controls',
    methods: {
        getDate: function () {
            this.$emit('dates', [this.fromDate,this.toDate])
        },
        handleFileUpload: function () {
            this.files = this.$refs.files.files;	    
        },
        submitFiles: function () {
            let formData = new FormData();
            for ( let i = 0; i < this.files.length; i++ ) {
                let file = this.files[i];
                formData.append('files[' + i + ']', file);
            }

            axios.post( 'http://localhost:8000/mapVisual/upload-files/',
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
          files: ''
      }
    }

}
</script>

<style>
  
</style>
