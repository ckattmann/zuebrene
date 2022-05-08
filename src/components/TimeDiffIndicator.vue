<template lang='pug'>

#timediffindicator-container
    div.text(:style="{ backgroundColor: bColor }") 
        span online &nbsp
        span {{ ms_to_human(timeDiffMs) }}

</template>

<script>
export default {
    name: 'TimeDiffIndicator',
    props: {
        timestamp_s: Number,
    },
    data() {
        return {
            bColor: 'darkslategray',
            timeDiffMs: 0,
        }

    },
    computed: {
        dateTimeDiff() {
            let date = new Date(this.timestamp_s)
            let now = new Date()
            return (now-date)
        },
    },
    methods: {
        computeTimeDiffMs() {
            let date = new Date(this.timestamp_s)
            let now = new Date()
            this.timeDiffMs = (now - date)
        },
        ms_to_human(ms) {
            if (ms < 1000) {
                this.bColor = "green"
                return ms + ' ms ago'
            }
            if (ms < 15*1000) {
                this.bColor = "green"
                return (ms/1000).toFixed(0) + ' s ago'
            } 
            if (ms < 60*1000) {
                this.bColor = "olivedrab"
                return (ms/1000).toFixed(0) + ' s ago'
            }
            // 1m - 1h
            if (ms < 60*60*1000) {
                this.bColor = "orangered"
                return (ms/1000/60).toFixed(0) + ' mins ago'
            }
            // 1h - 1d
            if (ms < 24*60*60*1000) {
                this.bColor = "orangered"
                return (ms/1000/60/60).toFixed(0) + ' hours ago'
            }
            // 1d - ...
            else {
                this.bColor = "orangered"
                return (ms/1000/60/60/24).toFixed(0) + ' days ago'
            }
        }
    },
    mounted() {
        setInterval(() => {
            this.computeTimeDiffMs()
        }, 1000)

    }
}
</script>

<style lang='sass' scoped>

.text
    padding: 1px 5px
    // background-color: darkslategray
    color: white
    font-size: 0.9em
    border-radius: 5px
        

</style>
