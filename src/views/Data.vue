<template lang='pug'>

#container
    //- Plot
    PlotGroup

</template>

<script>
import PlotGroup from '@/components/PlotGroup.vue';
import Plot from '@/components/Plot.vue';

export default {
    name: 'Data',
    components: {
        Plot,
        PlotGroup
    },
    data() {
        return {}
    },
    methods: {
    },
    mounted() {
    }
}
</script>

<style scoped>

#container {
    width: 100%;
    background-color: whitesmoke;
}

</style>
