<template lang='pug'>

#map-container
    span fajsldfkj
    #map

</template>

<script>

import LeafletCSS from 'leaflet/dist/leaflet.css';
import Leaflet from 'leaflet'

export default {
    name: 'Map',
    components: {},
    mounted() {
        let map = Leaflet.map('map').setView([51.505, -0.09], 6);
        Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);
    }
}
</script>

<style scoped>

#map-container {
    width: 100%;
    /* height: 1024px; */
    position: absolute;
    bottom: 0;
    top: 60px;
    left: 0;
    right: 0;
}
#map {
    position: absolute;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    z-index: 0;
}

</style>
