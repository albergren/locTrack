<template>
  <div>
    <p>Opacity</p>
    <div class="slidecontainer">
  <input type="range" min="1" max="10" value="5" class="slider" id="myRange" ref="sliderValue"  v-on:change="changeOpacity()">
</div>
  </div>
</template>
    
<script>
  export default {
      name: 'Options',
      data: function() {
          return {
  
          };
      },
      methods: {
          changeOpacity: function () {
              this.$emit('opacity', this.$refs.sliderValue.value / 10);
          },
      },
  }
</script>

<style>

</style>

