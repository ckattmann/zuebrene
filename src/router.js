import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

import Map from './views/Map.vue'
import Devices from './views/Devices.vue'
import Data from './views/Data.vue'
import Login from './views/Login.vue'

Vue.use(Router);

let router = new Router({
    mode: 'history',
	base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            redirect: '/login'
        }, 
        {
            path: '/login',
            component: Login
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

router.beforeEach((to, from, next) => {
    // console.log(to)
    // Everybody can /login:
    if  (to.path == '/login') { return next() }

    if (!store.state.login.username) { return next('/login')}

	// If the route requires no auth, no problem:
	// if (!to.meta.requiresAuth) { return next() }

	// Get the users' JWT:
	// let token = localStorage.getItem('jwt-token')
	// let decodedToken = jwt.decode(token)

	// If he hasnt got one, send him to login:
	// if (!token || !decodedToken) { return next('/login') }

	// If he has a token and its expired, send him to login:
	// if (new Date() > decodedToken.exp * 1000) { return next('/login') }

	// If route requires admin and user isnt admin, send him to login:
	// if (to.meta.requiresAdmin && !decodedToken.user_claims.admin) { return next('/login') }

	// Check if Vuex-Store reflects the token, otherwise renew store:
	// if (!store.state.user.username) {
	// 	store.commit('setUser', token) 
	// }

	// axios.defaults.headers.common = { 'Authorization': 'Bearer ' + token , 'Cache-Control': 'no-cache'}
	// axios.interceptors.response.use(response => { return response }, error => { if (error.response.status == 422 || error.response.status == 401) { return next('/login') } })

	return next()
})

export default router