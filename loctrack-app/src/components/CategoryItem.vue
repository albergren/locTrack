<template>
    <span>
    <div>
    <span @click="toggleChildren"> {{ categoryName  }} </span>
    <remove-category-button v-bind:categoryID="categoryID"/>

</div>
            <ul v-if="showChildren">       
                <li v-for="category in categories" :key="category.pk" >
                    <div  @click="toggleChildren(category.pk)"> {{  category.fields.name }}</div>
                        <category-item v-bind:parentID="category.pk" />
     
</li>
    <li>
           <add-category-button v-bind:parentID="categoryID"/>
     
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
          'categoryID', 'categoryName' 
      ],
      data: function () {
          return {
              categories : [],
              showChildren: false,
          };
      },

      mounted() {
          this.getChildCategories(this.categoryID);
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
          
          toggleChildren() {
              this.showChildren = !this.showChildren;
          }


      
      },
}
</script>

<style>

</style>
