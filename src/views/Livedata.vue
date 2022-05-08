<template lang='pug'>

#container
    #devices-container
        //- div {{ $store.state.livedata }}
        .device-card(v-for='data, sitename in $store.state.livedata')
            //- div {{ new Date(data.time).toISOString() }}
            //- div {{ data }}
            //- div {{  }}
            .card-header
                div.sitename {{ getSiteName(sitename) }}
                TimeDiffIndicator(:timestamp_s='data.time')
                img.sleeve-image(src="@/assets/Muffe_klein.svg", width='200px')
            .card-info
                .card-info-top
                    div.date {{ new Date(data.time).toLocaleString('de-DE', {timeZone: 'Europe/Berlin'}) }}

                table
                    tr 
                    tr
                        td.data-name {{ getValueName(sitename, 'pd1_pC') }}
                        td.data-value(:class="{alert : data.pd1_pC > 10}") {{ Math.round(data.pd1_pC*10)/10 }} pC 
                        //- td.spacer
                        //- td.data-name {{ getValueName(sitename, 'pd2_pC') }}
                        //- td.data-value(:class="{alert : data.pd2_pC > 10}") {{ Math.round(data.pd2_pC*10)/10 }} pC 
                    tr
                        td.data-name {{ getValueName(sitename, 'temperature1_C') }}
                        td.data-value {{ Math.round(data.temperature1_C*10)/10 }} °C
                        td.spacer
                        td.data-name {{ getValueName(sitename, 'temperature2_C') }}
                        td.data-value {{ Math.round(data.temperature2_C*10)/10 }} °C
                        td.spacer
                        td.data-name {{ getValueName(sitename, 'temperature3_C') }}
                        td.data-value {{ Math.round(data.temperature3_C*10)/10 }} °C
                    tr
                        td.data-name {{ getValueName(sitename, 'temperature4_C') }}
                        td.data-value {{ Math.round(data.temperature4_C*10)/10 }} °C
                        td.spacer
                        td.data-name {{ getValueName(sitename, 'temperature5_C') }}
                        td.data-value {{ Math.round(data.temperature5_C*10)/10 }} °C
                        td.spacer
                        td.data-name {{ getValueName(sitename, 'temperature6_C') }}
                        td.data-value {{ Math.round(data.temperature6_C*10)/10 }} °C
                    tr
                        td.data-name {{ getValueName(sitename, 'primary_current_A') }}
                        td.data-value {{ Math.round(data.primary_current_A*6)/10 }} A
                        td.spacer
                        td.data-name {{ getValueName(sitename, 'sync_freq_Hz') }}
                        td.data-value {{ Math.round(data.sync_freq_Hz*100)/100 }} Hz

</template>

<script>

import TimeDiffIndicator from '@/components/TimeDiffIndicator.vue'

export default {
    name: 'Livedata',
    components: {
        TimeDiffIndicator
    },
    computed: {
        config: function() {
            return this.$store.state.config
        }
    },
    methods: {
        toDatetimeString: function(datetime) {
            return new Date(datetime).toISOString() 
        },
        getSiteName(sitename) {
            return (this.config[sitename] && this.config[sitename].name) || sitename
        },
        getValueName(sitename, valuename) {
            return (this.config[sitename]
                && this.config[sitename].name
                && this.config[sitename].values
                && this.config[sitename].values[valuename]
                && this.config[sitename].values[valuename].name)
                || valuename
        }
    },
    mounted() {}
}
</script>

<style scoped>

#container {
    /* padding-top: 60px; */
    width: 100%;
    /* min-height: calc(100vh - 60px); */
    background-color: whitesmoke;
}
.device-card {
    display: flex;
    background-color: white;
    margin: 10px;
    margin-bottom: 5px;
    box-shadow: 1px 1px 4px 1px rgba(0,0,0,0.2);
    padding: 5px;
}

.sleeve-image {
    margin: 10px;
    margin-top: 20px;
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

.card-info-top {
    display: flex;
    margin-bottom: 5px;
}

.date {
    margin-right: 10px;
    padding: 1px 5px;
    background-color: whitesmoke;
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
    margin-bottom: 3px;
}

td.data-name {
    padding-top: 0;
    padding-bottom: 0;
    text-align: left;
    padding-right: 20px;
    margin-left: 10px;
    width: 150px;
}

td.data-value {
    padding-top: 0;
    padding-bottom: 0;
    padding-right: 5px;
    width: 80px;
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
