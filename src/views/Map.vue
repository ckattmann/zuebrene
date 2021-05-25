<template lang='pug'>

#map-container
    #map

</template>

<script>

import Vue from 'vue'
import store from '@/store.js'
import LeafletCSS from 'leaflet/dist/leaflet.css'
import Leaflet from 'leaflet'
import MapPopup from '@/components/MapPopup.vue'

export default {
    name: 'Map',
    components: {
        MapPopup
    },
    data: function() {
        return {
            map: null,
            latlon_array: []
        }
    },
    methods: {

    },
    mounted() {
        this.map = Leaflet.map('map').setView([55.62400761775817, 12.514305699384524], 12);
        Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(this.map);
        this.$store.dispatch('getLiveData').then(() => {
            for (let sitename in this.$store.state.sites) {
                let site = this.$store.state.sites[sitename]
                this.latlon_array.push(site.latlon)
                let fillColor = site.pd_value > 10 ? 'red' : 'green'
                let circle = Leaflet.circle(site.latlon, {radius: 50, stroke: false, fillColor: site.pd_value > 10 ? 'red' : 'green', fillOpacity: 1})
                circle.addTo(this.map)
                // Add Popup:
                let DataBlock;
                DataBlock = Vue.extend(MapPopup);
                let dataBlockInstance = new DataBlock({ parent:this, propsData: {sitename: sitename } });
                dataBlockInstance.$mount()
                let popup = circle.bindPopup(dataBlockInstance.$el, {
                    closeButton: true
                });


                circle.on('mouseover', function(e) {this.openPopup()} );
                circle.on('mouseout', function(e) {this.closePopup()} );
            }
            let line = Leaflet.polyline(this.latlon_array, {smoothFactor: 1.0, color: 'black', weight: 5})
            line.addTo(this.map)
            line.bringToBack()
            console.log(this.map)
            this.map.fitBounds(this.latlon_array)
        })
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
