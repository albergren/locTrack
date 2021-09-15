<template>
    <span>
    <div>
    <span class="subbutton" @click="toggleChildren"> {{ categoryName  }}

    <div style="float:right">
    <remove-category-button v-bind:categoryID="categoryID"/>
    </div>
        <div style="float:right">
           <add-category-button v-bind:categoryID="categoryID"/>
    
</div>
</span>

</div>
            <div v-if="showChildren">       
                <div v-for="category in categories" :key="category.pk" >
                        <category-item v-bind:categoryID="category.pk"  v-bind:categoryName="category.fields.name"/>
     
</div>

           </div>

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
          console.log(this.categoryID);
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
