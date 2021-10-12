<template lang='pug'>

#container
    #devices-container
        .device-card(v-for='site, sitename in $store.state.sites')
            .card-header
                div.sitename {{ site.name }}
                img.sleeve-image(src="@/assets/Muffe_klein.svg", width='200px')
            .card-info
                table
                    tr
                        td.data-name PD Value U
                        td.data-value(:class="{alert : site.pd_value > 10}") {{ Math.round(site.pd_value*10)/10 }} pC 
                        td.spacer
                        td.data-name PD Value V
                        td.data-value(:class="{alert : site.pd_value > 10}") {{ Math.round(site.pd_value*10)/10 }} pC 
                        td.spacer
                        td.data-name PD Value W
                        td.data-value(:class="{alert : site.pd_value > 10}") {{ Math.round(site.pd_value*10)/10 }} pC 
                    tr
                        td.data-name Temperature
                        td.data-value {{ Math.round(site.temperature*10)/10 }} °C
                        td.spacer

</template>

<script>

export default {
    name: 'Devices',
    components: {
    },
    mounted() {
    }
}
</script>

<style>

#container {
    padding-top: 60px;
    width: 100%;
    min-height: calc(100vh - 60px);
    background-color: whitesmoke;
}
.device-card {
    display: flex;
    background-color: white;
    margin: 10px;
    margin-bottom: 5px;
    box-shadow: 1px 1px 4px 1px rgba(0,0,0,0.2);
}

.sleeve-image {
    margin: 10px;
}

.card-info {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding-left: 20px;
    /* background-color:yellowgreen; */
}

.card-header {
    margin: 5px;
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.sitename {
    font-weight: bold;
}

td.data-name {
    padding-top: 0;
    padding-bottom: 0;
    text-align: left;
    padding-right: 20px;
    margin-left: 10px;
}

td.data-value {
    padding-top: 0;
    padding-bottom: 0;
    width: 70px;
    text-align: right;
    background-color: whitesmoke;
}
td.data-value.alert {
    color: red;
    font-weight: bold;
}
td.spacer {
    width: 10px;
}
.data-valuebar-container {
    width: 100px;
    /* background-color: green; */
}

.data-valuebar {
    /* width: 100px; */
    background-color: green;
}

</style>
