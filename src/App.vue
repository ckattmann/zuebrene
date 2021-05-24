<template lang='pug'>

#app
    Topbar
    router-view

</template>

<script>
import Topbar from './components/Topbar.vue'

export default {
  name: 'App',
  components: {
    Map,
    Topbar
  },
  mounted() {
  }
}
</script>

<style>

@font-face {
    font-family: 'Open Sans';
    src: url('assets/OpenSans-Regular.ttf');
}

html, body {
  margin: 0;
  min-height: 100%;
}

#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}

</style>
