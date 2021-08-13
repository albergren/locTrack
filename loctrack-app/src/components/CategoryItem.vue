<template>
    <span>
       <ul>
           <li v-for="category in categories" :key="category.fields.pk" >
    
               {{  category.fields.name }}
               <add-category-button v-bind:parentID="category.pk"/>
               <remove-category-button v-bind:categoryID="category.pk"/>
               <category-item v-bind:parentID="category.pk"/>

           </li>
       </ul>   
    </span>
</template>

<script>

import axios from 'axios';
import AddCategoryButton from './AddCategoryButton.vue'
import RemoveCategoryButton from './RemoveCategoryButton.vue'

  export default {
      name: 'CategoryItem',
      components: {
  'add-category-button': AddCategoryButton,
  'remove-category-button': RemoveCategoryButton,

      },
      props: [
          'parentID'
      ],
      data: function () {
          return {
          categories : [],
          };
      },

      mounted() {
  this.getChildCategories(this.parentID);
        
      },
      
      methods: {

          getChildCategories: function (id) {            
              axios.get('http://localhost:8000/mapVisual/child-categories', {params: {  categoryID: id }}
                       ).then(resp => {
                           let data = JSON.parse(resp.data);
                           this.categories = data;                           
                       }).catch(function() {
                           console.log('Failure!');
                       });
          },

      
      },
}
</script>

<style>

</style>
