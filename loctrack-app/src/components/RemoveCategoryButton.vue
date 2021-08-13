<template>
  <span>
 <button  v-on:click="removeCategory">Remove</button>
    
  
</span>
</template>

<script>
  import axios from 'axios';

  export default {
      name: 'RemoveCategoryButton',
      props: [
          'categoryID'
      ],
      data: function () {
          return {
          };
      },
      methods: {
          removeCategory: function () {
              console.log(this.categoryID);
              axios.post( 'http://localhost:8000/mapVisual/remove-category/',
                          JSON.stringify( {
                              categoryID: this.categoryID,
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
      },
  }
</script>

<style>

</style>
