import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        login: {
            username: ''
        },
        sites: {},
        livedata: {},
        config: {}
    },
    mutations: {
        updateSites(state, sites) {
            state.sites = sites
        },
        updateLiveData(state, livedata) {
            state.livedata = livedata
        },
        updateConfig(state, config) {
            state.config = config
        }
    },
    actions: {
        login(state, payload) {
            let oauth2FormData = new FormData()
            oauth2FormData.append('username', payload.username)
            oauth2FormData.append('password', payload.password)
            return axios.post('/api/token', oauth2FormData)
                .then(response => {
                    let token = response.data.token
                    axios.defaults.headers.common = { 'Authorization': 'Bearer ' + token, 'Cache-Control': 'no-cache'}
                    axios.interceptors.response.use(response => { return response }, error => { if (error.response.status == 422 || error.response.status == 401) { return next('/login') } })
                    this.state.login.username = payload.username
                    // state.commit('setUser', token)
                    // state.dispatch('getDevices');
                    // state.dispatch('getMeasurements');
                })
		},
        // getSites(state) {
        //     return axios.get("/api/sites").then(response => {
        //         state.commit('updateSites', response.data)
        //     })
        // },
        async getConfig(state) {
            const response = await fetch('api/config')
            const config = await response.json()
            state.commit('updateConfig', config)

        },
        async getLiveData(state) {
                const response = await axios.get("/api/livedata")
            // console.log(response)
            state.commit('updateSites', response.data)
        },
        async getLiveData2(state) {
                const response = await axios.get("/api/livedata2")
            // console.log(response)
            state.commit('updateLiveData', response.data)
        },
    }
})
