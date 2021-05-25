import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        sites: {}
    },
    mutations: {
        updateSites(state, sites) {
            state.sites = sites
        }
    },
    actions: {
        // getSites(state) {
        //     return axios.get("/api/sites").then(response => {
        //         state.commit('updateSites', response.data)
        //     })
        // },
        async getLiveData(state) {
            const response = await axios.get("/api/livedata")
            // console.log(response)
            state.commit('updateSites', response.data)
        },
    }
})
