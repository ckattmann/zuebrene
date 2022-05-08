<template lang='pug'>

#group-container
    #plot-header
        ButtonGroup.bgroup(:items='measurements', v-model='measurement')
        //- ButtonGroup.bgroup(:items='field_keys', v-model='field_key')
        ButtonGroup.bgroup(:items='timeframes', v-model='timeframe')
        ButtonGroup.bgroup(:items='aggregations', v-model='aggregation')
    #plot
        SinglePlot(
            :measurementId='measurement.id',
            :plotData="data",
            :plotKeys="plot1keys",
            plotyAxisName='Temperature'
            unit='°C')
        SinglePlot(
            :measurementId='measurement.id',
            :plotData="data",
            :plotKeys="[{'key':'primary_current_A','label':'Current', 'unit':'A'}]",
            plotyAxisName='Current',
            unit='A'
        )
        SinglePlot(
            :measurementId='measurement.id',
            :plotData="data",
            :plotKeys="[{'key':'sync_freq_Hz','label':'Sync Frequency', 'unit':'Hz'}]",
            plotyAxisName='Sync Freq',
            unit='Hz'
        )

</template>

<script>

    //- :plotKeys="[{'key':'temperature1_C','label':'Temperature2', 'unit':'°C'}, {'key':'temperature2_C','label':'Temperature', 'unit':'°C'}, {'key':'temperature3_C','label':'Temperature', 'unit':'°C'}, {'key':'temperature4_C','label':'Temperature', 'unit':'°C'}, {'key':'temperature5_C','label':'Temperature', 'unit':'°C'}, {'key':'temperature6_C','label':'Temperature', 'unit':'°C'}]",

import axios from 'axios'
import uPlot from 'uplot'
import uPlotCSS from "uplot/dist/uPlot.min.css"

import SinglePlot from './SinglePlot.vue'
import ButtonGroup from './ButtonGroup.vue'

export default {
    components: {
        ButtonGroup,
        SinglePlot
    },
    props: {

    },
    data() {
        return {
            plot1keys: [ 
                {'key': 'temperature1_C', 'unit':'°C', 'color':'red'},
                {'key': 'temperature2_C', 'unit':'°C', 'color':'green'},
                {'key': 'temperature3_C', 'unit':'°C', 'color':'blue'},
                {'key': 'temperature4_C', 'unit':'°C', 'color':'black'},
                {'key': 'temperature5_C', 'unit':'°C', 'color':'darkslategray'},
                {'key': 'temperature6_C', 'unit':'°C', 'color':'orange'},
            ],
            measurements: [
                {'name':'Muffe 1', 'id':'client_0'},{'name':'Muffe 2', 'id':'client_1'}
            ],
            measurement: {'name':'client_0', 'id':'client_0'},
            field_keys: [
                {'name': 'T1', 'id': 'temperature1_C'},
                {'name': 'T2', 'id': 'temperature2_C'},
                {'name': 'T3', 'id': 'temperature3_C'},
                {'name': 'T4', 'id': 'temperature4_C'},
                {'name': 'T5', 'id': 'temperature5_C'},
                {'name': 'T6', 'id': 'temperature6_C'},
                {'name': 'Primary Current', 'id': 'primary_current_A'},
                {'name': 'Sync Freq.', 'id': 'sync_freq_Hz'},
                {'name': 'PD 1', 'id': 'pd1_pC'},
                {'name': 'PD 2', 'id': 'pd2_pC'},
            ],
            field_key: {'name': 'Temperature 1', 'id': 'temperature1_C'},
            timeframes: [
                {'name': 'Today', 'id': 'today'},
                {'name': 'This week', 'id': 'thisweek'},
                {'name': 'Last 2 Weeks', 'id': 'last2weeks'},
            ],
            timeframe: {'name': 'Today', 'id': 'today'},
            aggregations: [
                {'name': '10 Seconds', 'id': '10s'},
                {'name': '1 Minute', 'id': '1m'},
                {'name': '10 Minutes', 'id': '10m'},
            ],
            aggregation: {'name': '10 Seconds', 'id': '10s'},
            data : {},
        };
    }, 
    computed: {
        config: function() {
            return this.$store.state.config
        }
    },
    methods: {
        getData() {
            return axios.get('/api/betterHistoricData', {params: 
                { 
                    measurement: this.measurement.id,
                    timeframe: this.timeframe.id,
                    aggregation: this.aggregation.id
                }}).then((response) => {
                    this.data = response.data;
            })
        }
    },
    watch: {
        measurement: function(to, from) { this.getData() },
        field_key: function(to, from) { this.setData() },
        timeframe: function(to, from) { this.getData() },
        aggregation: function(to, from) { this.getData() },
    },
    mounted() {
        this.getData();
    }
}
</script>

<style scoped>

#group-container {
    margin-top: 10px;
    background-color: white;
    /* border: 1px solid black; */
    margin: 10px;
    padding: 10px;
    box-shadow: 1px 1px 4px 1px rgba(0,0,0,0.2);
}
#plot-header {
    display: flex;
    flex-direction: column;
    align-items: flex-start;

}
.bgroup {
    margin-bottom: 5px;
}

</style>