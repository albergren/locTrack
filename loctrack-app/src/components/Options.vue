<template>

    <div>
        <div class="large-12 medium-12 small-12 ">
            <h3>File upload</h3>
                <input type="file" id="files" ref="files" multiple v-on:change="handleFileUpload()"/>
                <button v-on:click="submitFiles">Submit</button>
    
        </div>
        <h3>Show dates</h3>
        <p>From:</p>
            <input type="date" v-model="fromDate">
        <p>To:</p>
            <input type="date" v-model="toDate">
        <button v-on:click="getDate">Go</button>
   
        <h3>Opacity</h3>
        <div>
            <input type="range" min="1" max="10" value="5" class="slider" id="opacityRange" ref="sliderValue"  v-on:change="changeOpacity()">
        </div>
    
        <h3>Locations</h3>
        <new-location/>
        <table>
            <tr v-for="location in locations" :key="location.properties.pk" >
                <td >
                    {{  location.properties.name }}
                </td>
                <td>
                    <input type="checkbox"  :value=location.properties.pk v-model="checkedLocations">
                </td>
                <td>
                    <button v-on:click="editLocation">Edit</button>

                </td>
            </tr>
        </table>


        <h3>Categories</h3>
        <category-item v-bind:parentID="null"/>
        <add-category-button v-bind:parentID="null"/>
        <remove-category-button v-bind:parentID="null"/>

  </div>
</template>
    
<script>
import EventBus from '../event-bus';
import axios from 'axios';
import CategoryItem from './CategoryItem.vue'
import AddCategoryButton from './AddCategoryButton.vue'
import RemoveCategoryButton from './RemoveCategoryButton.vue'
import NewLocation from './NewLocation.vue'



export default {
    name: 'Options',
    components: {
        'category-item': CategoryItem,
        'add-category-button': AddCategoryButton,
        'remove-category-button': RemoveCategoryButton,
	'new-location': NewLocation,
        
    },
    data: function() {
        return {
            fromDate: '',
            toDate: '',
            locations: [],
            checkedLocations: [],
            parentCategory: null,

            files: '',


        };
    },

    watch: {
        checkedLocations: function () {
            EventBus.$emit('checkedLocations', this.checkedLocations);
        },
        
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
            console.log("getAllLocations");
            
            axios.get( 'http://localhost:8000/mapVisual/all-locations/'
                     ).then(resp =>  {
                         this.locations = [];
                         let data = JSON.parse(resp.data);              
                         this.locations = data.features;
                         EventBus.$emit('locationData', this.locations);
                     }).catch(function() {
                         console.log('Failure!');
                     })
        },
        
        editLocation: function () {
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
    
    created() {
        
        EventBus.$on('locationAdded', this.getAllLocations);
    },
}

</script>

<style>

</style>

