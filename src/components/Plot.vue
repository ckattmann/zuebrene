<template lang='pug'>

#plot-container
    #plot

</template>

<script>

import axios from 'axios'
import uPlot from 'uplot'
import uPlotCSS from "uplot/dist/uPlot.min.css";

export default {
    props: {

    },
    data() {
        return {
            plot: null,
            uPlotOptions: {
                id: "plot",
				tzDate: ts => uPlot.tzDate(new Date(ts * 1e3), 'Europe/Berlin'),
                series: [
                    {
                        value: (self, rawValue) => new Date(rawValue * 1e3),
                    }, // Time
                    {
                        value: (self, rawValue) => Math.round(rawValue) + '°C',
                        label: 'Temperature',
                        stroke: 'red',
                        scale: 'T',
                        width: 1.5

                    }
                ],
                scales: {
                    'x': {
                        time: true,
                        key: 'Time'
                        // values: (self, ticks) => ticks.map(rawValue => rawValue+' ms')
                    },
                    'T': {}
                },
                axes: [
                    { show: true, label: "Time", labelFont: "14px Open Sans" },
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
    methods: {
        getData() {
            axios.get('/api/betterHistoricData').then((response) => {
                console.log(response.data);
                this.plot.setData(response.data)
            })

        },
        initPlot() {
            document.getElementById('plot').innerHTML = '';
            const container = document.getElementById('plot');
            this.uPlotOptions.width = container.scrollWidth-30;
            this.uPlotOptions.height = 300;
            let initialData = this.uPlotOptions.series.map(s => [0,1])
            initialData.unshift([0]);
            this.plot = new uPlot(this.uPlotOptions, initialData, document.getElementById('plot'));
            // console.log(this.plot);
        },
    },
    mounted() {
        this.getData();
        this.initPlot();
    }
}
</script>

<style>

#plot-container {
    margin-top: 10px;
    background-color: white;
    /* border: 1px solid black; */
    margin: 10px;
    padding: 10px;
    box-shadow: 1px 1px 4px 1px rgba(0,0,0,0.2);
}

</style>