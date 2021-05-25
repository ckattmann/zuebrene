import Vue from 'vue'
import Router from 'vue-router'

import Map from './views/Map.vue'
import Devices from './views/Devices.vue'
import Data from './views/Data.vue'

Vue.use(Router);

let router = new Router({
    mode: 'history',
	base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            redirect: '/map'
        },
        {
            path: '/map',
            component: Map
        },
        {
            path: '/devices',
            component: Devices
        },
        {
            path: '/data',
            component: Data
        }
    ]
})

export default router