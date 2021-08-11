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


    <p>Categories</p>

    <button v-if="!addingNewCategory" v-on:click="newCategory">New location</button>
    
    <div v-if="addingNewCategory">
    <br>
    <div>
      <form>
        <label>New Category
          <input type="text" id="categoryName" v-model="newCategoryName" placeholder="Name"/>
          <input type="color"  id="categoryColor" v-model="newCategoryColor"/> 

        </label>
      <br>
      <button type="button" v-on:click="addCategory">Add</button>
    <button type="button" v-on:click="cancelNewCategory">Cancel</button> 
      </form>
    </div>
    </div>
    <table>
    <tr v-for="category in categories" :key="category.fields.pk" >
    <td >
    {{  category.fields.name }}
      <button type="button" v-on:click="addCategory">Add</button>

    </td>

    </tr>
  
    </table>
    
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
            checkedLocations: [],
            categories : [],
            addingNewCategory: false,
            newCategoryName: '',
            newCategoryColor: '#a46fe2',
            parentCategory: null,
        };
    },

    watch: {
        checkedLocations: function () {
            EventBus.$emit('checkedLocations', this.checkedLocations);
        },
        
    },
    mounted() {
        this.getAllLocations();
        this.getAllCategories();
        
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
            
            axios.get( 'http://localhost:8000/mapVisual/get-all-locations/'
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

        newCategory: function (){
            this.addingNewCategory = true;
        },

        addCategory: function () {
            axios.post( 'http://localhost:8000/mapVisual/new-category/',
                        JSON.stringify( {
                            name: this.newCategoryName,
                            color: this.newCategoryColor,
                            parent: this.parentCategory,
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
        cancelNewCategory: function () {
            this.addingNewCategory = false;
            
        },

        getAllCategories: function () {
            console.log("getAllCategories");
            axios.get('http://localhost:8000/mapVisual/all-categories/'
                     ).then(resp => {
                       this.categories = [];
                         let data = JSON.parse(resp.data);
                         this.categories = data;
  
                     }).catch(function() {
                                        console.log('Failure!');
                     })
        },
    },
    
    created() {
        
        EventBus.$on('locationAdded', this.getAllLocations);
    },
}

</script>

<style>

</style>

