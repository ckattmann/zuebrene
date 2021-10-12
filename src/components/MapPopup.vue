<template lang='pug'>

#popup-container
    div.bold {{ $store.state.sites[sitename].name }}
    div Type: {{ deviceState.type }}
    div PD Value U {{ Math.round($store.state.sites[sitename].pd_value*10)/10 }} pC 
    div PD Value S {{ Math.round($store.state.sites[sitename].pd_value*10)/10 }} pC 
    div PD Value T {{ Math.round($store.state.sites[sitename].pd_value*10)/10 }} pC 
    div Temperature {{ Math.round($store.state.sites[sitename].temperature*10)/10 }} °C
  
</template>

<script>
export default {
    props: {
        // deviceState: Object,
        sitename: String
    },
    data() {
        return {
            deviceState: {}
        }
    },
    mounted() {
        console.log(this.$store.state);
        this.deviceState = this.$store.state.sites[this.sitename]
        console.log(this.deviceState);
    }

}
</script>

<style>
.bold {
    font-weight: bold;
}
</style>