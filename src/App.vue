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
    methods: {
        updateLiveData: function() {
            this.$store.dispatch('getLiveData')
        }
    },
    mounted() {
        setInterval(this.updateLiveData, 1000)
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
    padding: 0;
    /* max-width: 100%; */
    /* overflow: hidden; */
    min-height: 100%;
}

#app {
    font-family: 'Open Sans', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /* min-height: 100vh;
    max-height: 100vh; */
}

.leaflet-tile-pane {
    opacity: 0.8 !important;
    filter: saturate(0.5) grayscale(0.5);
}

</style>
