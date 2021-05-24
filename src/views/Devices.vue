<template lang='pug'>

#map-container
    span abcd
    #map

</template>

<script>

import LeafletCSS from 'leaflet/dist/leaflet.css';
import Leaflet from 'leaflet'

export default {
  name: 'Devices',
  components: {
  },
  mounted() {
    let map = Leaflet.map('map').setView([51.505, -0.09], 6);
    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);
  }
}
</script>

<style>

#map-container {
  width: 100%;
}
#map {
    height: 100%;
    width: 100%;
}

</style>
