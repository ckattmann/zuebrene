<template lang='pug'>

#container
    Plot

</template>

<script>
import Plot from '@/components/Plot.vue';

export default {
    name: 'Data',
    components: {
        Plot
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

<style>

#container {
    padding-top: 60px;
    width: 100%;
    min-height: calc(100vh - 60px);
    background-color: whitesmoke;
}

</style>
