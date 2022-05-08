<template lang='pug'>

#app
    Topbar(v-if='$store.state.login.username')
    router-view

</template>

<script>
import Topbar from './components/Topbar.vue'
// import Livedata from './components/Livedata.vue'

export default {
    name: 'App',
    components: {
        // Livedata,
        Topbar
    },
    methods: {
        updateConfig: function() {
            this.$store.dispatch('getConfig')
        },
        updateLiveData2: function() {
            this.$store.dispatch('getLiveData2')
        }
    },
    mounted() {
        if (this.$store.state.login.username === '') {

        }
        this.updateConfig()
        setInterval(this.updateConfig, 10000)
        setInterval(this.updateLiveData2, 2000)
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
body {
    padding-top: 60px;
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
