<template lang='pug'>

#plot-container
    //- #plot-header
        //- ButtonGroup.bgroup(:items='measurements', v-model='measurement')
        //- ButtonGroup.bgroup(:items='field_keys', v-model='field_key')
        //- ButtonGroup.bgroup(:items='timeframes', v-model='timeframe')
        //- ButtonGroup.bgroup(:items='aggregations', v-model='aggregation')

    //- This id needs to be unique:
    div(:id='uuid')

</template>

<script>

import axios from 'axios'
import uPlot from 'uplot'
import uPlotCSS from "uplot/dist/uPlot.min.css"
import ButtonGroup from './ButtonGroup.vue'

export default {
    components: {
        ButtonGroup,
    },
    props: {
        measurementId: String,
        plotData: Object,
        plotKeys: Array,
        plotyAxisName: String,
        unit: String
    },
    data() {
        return {
            uuid: Math.random().toString(36).replace(/[^a-z]+/g, '').substr(0, 5),
            plot: null,
            uPlotOptions: {
                id: "plot",
				tzDate: ts => uPlot.tzDate(new Date(ts * 1e3), 'Europe/Berlin'),
                series: [
                    {
                        value: "{DD}.{MM}.{YYYY} {HH}:{mm}:{ss}"
                    } // Time
                ],
                scales: {
                    'x': {
                        time: true,
                        key: 'Time',
                    },
                    'T': {
                        range: [0,100]
                    }
                },
                axes: [
                    { 
                        show: true, label: "Time",
                        labelFont: "14px Open Sans", 
                        values: [
                            // tick incr          default           year                             month    day                        hour     min                sec       mode
                            [3600 * 24 * 365,   "{YYYY}",         null,                            null,    null,                      null,    null,              null,        1],
                            [3600 * 24 * 28,    "{MMM}",          "\n{YYYY}",                      null,    null,                      null,    null,              null,        1],
                            [3600 * 24,         "{DD}.{MM}.",     "\n{YYYY}",                      null,    null,                      null,    null,              null,        1],
                            [3600,              "{HH}:{mm}",      "\n{DD}.{MM}.{YYYY}",            null,    "\n{DD}.{MM}.",            null,    null,              null,        1],
                            [60,                "{HH}:{mm}",      "\n{DD}.{MM}.{YYYY}",            null,    "\n{DD}.{MM}.",            null,    null,              null,        1],
                            [1,                 ":{ss}",          "\n{DD}.{MM}.{YYYY} {HH}:{mm}",  null,    "\n{DD}.{MM} {hh}:{mm}",   null,    "\n{HH}:{mm}",     null,        1],
                            [0.001,             ":{ss}.{fff}",    "\n{DD}.{MM}/{YYYY} {HH}:{mm}",  null,    "\n{DD}.{MM} {HH}:{mm}",   null,    "\n{HH}:{mm}",     null,        1],
                        ]
                    },
                    {
                        scale: 'T',
                        label: "Temperature / °C",
                        labelFont: "14px Open Sans",
                        size: 60,
                        gap: 10, // between plot and ticks
                        // values: (self, ticks) => ticks.map(rawValue => lib.formatValue(rawValue, 'V'))
                    },
                ]
            }
        };
    },
    computed: {
        config: function() {
            return this.$store.state.config
        }
    },
    methods: {
        getValueName(sitename, valuename) {
            return (this.config[sitename]
                && this.config[sitename].name
                && this.config[sitename].values
                && this.config[sitename].values[valuename]
                && this.config[sitename].values[valuename].name)
                || valuename
        },
        setData() {
            let data = []
            data.push(this.plotData.time)
            for (let key of this.plotKeys) 
                data.push(this.plotData[key.key])
            this.plot.setData(data)
            let i = 1
            for (let key of this.plotKeys) {
                console.log(this.getValueName(this.measurementId, key.key))
                this.uPlotOptions.series[i].label = this.getValueName(this.measurementId, key.key)
                i += 1
            }
            // this.plot.redraw()
        },
        initPlot() {
            for (let key of this.plotKeys) {
                this.uPlotOptions.series.push({
                    value: (self, rawValue) => Math.round(rawValue) + ' ' + this.unit,
                    label: this.getValueName(this.measurementId, key.key),
                    stroke: key.color || 'black',
                    scale: 'T',
                    width: 1.5
                })
            }
            console.log(this.uPlotOptions.series);

            this.uPlotOptions.axes[1].label = this.plotyAxisName + ' / ' + this.unit

            document.getElementById(this.uuid).innerHTML = '';
            const container = document.getElementById(this.uuid);
            this.uPlotOptions.width = container.scrollWidth-30;
            this.uPlotOptions.height = 300;

            let initialData = this.uPlotOptions.series.map(s => [0,1])
            initialData.unshift([0]);

            this.plot = new uPlot(this.uPlotOptions, initialData, document.getElementById(this.uuid));
        },
    },
    watch: {
        plotData: function(to, from) { this.setData() },
        measurementId: function(to, from) { this.setData() },
        // field_key: function(to, from) { this.setData() },
        // timeframe: function(to, from) { this.getData() },
        // aggregation: function(to, from) { this.getData() },
    },
    mounted() {
        this.initPlot();
        this.setData();
    }
}
</script>

<style scoped>

#plot-container {
    margin-top: 10px;
    background-color: white;
    /* border: 1px solid black; */
    margin: 10px;
    padding: 10px;
    /* box-shadow: 1px 1px 4px 1px rgba(0,0,0,0.2); */
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