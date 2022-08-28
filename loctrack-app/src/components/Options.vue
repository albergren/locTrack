<template>

    <div>
            <h3>File upload</h3>
    <input type="file" id="files" ref="files" accept=".gpx" multiple v-on:change="handleFileUpload()"/>
                <br><button v-on:click="submitFiles">Submit</button>
    
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
                    <button v-on:click="editLocation">  <font-awesome-icon icon="edit" /></button>

                </td>
            </tr>
        </table>

  

    
    <div class="button" @click="toggleChildren">
<h3>
    <span  v-if="showChildren" class="arrow-icon"> <font-awesome-icon icon="chevron-down" /></span>
    <span  v-else class="arrow-icon"> <font-awesome-icon icon="chevron-right" /></span>
    Categories    
 <div  style="float:right">
            <add-category-button  @categoryAdded="getChildCategories(categoryID)" v-bind:categoryID="categoryID"/>
    </div>

</h3>

    </div>
        <div  v-if="showChildren">
    <div v-for="category in categories" :key="category.pk" >
                <category-item v-bind:categoryID="category.pk" v-bind:categoryName="category.fields.name"/>
</div>

    </div>
  </div>
</template>
    
<script>
import EventBus from '../event-bus';
import axios from 'axios';
import CategoryItem from './CategoryItem.vue'
import AddCategoryButton from './AddCategoryButton.vue'
import NewLocation from './NewLocation.vue'


export default {

    name: 'Options',
    components: {
        'category-item': CategoryItem,
        'add-category-button': AddCategoryButton,
	'new-location': NewLocation,
    },
    data: function() {
        
        return {
            fromDate: '',
            toDate: '',
            locations: [],
            checkedLocations: [],
            categoryID: null,
            categories: [],
            files: '',
            showChildren: false,
            
        };
    },

    watch: {
        checkedLocations: function () {
            EventBus.$emit('checkedLocations', this.checkedLocations);
        },
        
    },
    mounted() {
        this.getAllLocations();
        this.getChildCategories(null);
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

        getChildCategories: function (id) {
        axios.get('http://localhost:8000/mapVisual/child-categories', {params: {  categoryID: id }}
                       ).then(resp => {
                           let data = JSON.parse(resp.data);
                           this.categories = data;                           
                       }).catch(function() {
                           console.log('Failure!');
                       });
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

        toggleChildren() {
            this.showChildren = !this.showChildren;
            
          }

        
    },
    
    created() {
        
        EventBus.$on('locationAdded', this.getAllLocations);
    },
}

</script>

<style>
    .button {
	background-color: #4CAF50; /* Green */
	border: none;
	width: 100%;
	color: white;
	text-align: left;
	
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	padding-left:10px;
                padding: 10px;

	box-sizing:border-box;
	cursor: pointer;
    }

    .subbutton {
	background-color: darkgrey; /* Green */
        border: solid;
        border-width: 1px;
        border-color: lightgrey;
        border-left:none;
        border-right:none;
        width: 100%;
        color: white;
        text-align: left;
        
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        padding: 10px;
        padding-left:10px;

        box-sizing:border-box;
        cursor: pointer;
    }
    .arrow-icon {
        vertical-align: middle;
	margin-right: 8px;
    }
  
    .add-button {
        vertical-align: middle;
	margin-right: 8p;
    }
</style>

