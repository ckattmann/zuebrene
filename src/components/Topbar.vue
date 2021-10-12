<template lang='pug'>

div#topbar

    div.topbar-side
        div#bsslogo
            img(src="../assets/bss-logo.svg")
        div#title Zübrene Monitoring

        router-link.topline-button(to="/map") Map
        router-link.topline-button(to="/devices") Sites
        router-link.topline-button(to="/data") Data
        //- router-link.topline-button(v-if='this.$store.state.user.admin', to="/admindashboard") Admin

    div.topbar-side
        div#user
            div#usericon
                svg(width="34px" height="34px" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000")
                    g(stroke="white")
                        circle(stroke="white", stroke-width="50px" fill="none", cx="500", cy="500", r='450')
                        circle(stroke="white", stroke-width="50px" fill="none", cx="500", cy="350", r='150')
                        path(stroke="white", stroke-width="50px", fill="none", d="M250,750 A250,250,0,0,1,750,750")
                        //- path(v-if='this.$store.state.user.admin', stroke="gold", stroke-width="10px", stroke-linejoin="round", fill="gold", d="M350,250 v-200 l50,100 l50,-100 l50,100 l50,-100 l50,100 l50,-100 v200 Z")
            span#username {{this.$store.state.login.username}}
            //- div#user-dropdown
            //-     div#user-dropdown-item(@click="logout()") Logout

</template>


<script>

import router from '@/router.js';

export default {
    props: {},
    methods: {
        // logout() {
        //     this.$store.dispatch('logout');
        //     router.push('/login')
        // }
    }
}

</script>


<style lang='sass' scoped>

$mobile-breakpoint: 720px

#topbar
    height: 60px
    width: 100%
    position: fixed
    top: 0
    left: 0
    right: 0
    // max-width: 1400px
    background: linear-gradient(90deg, #086bc2, #2c9dd1)
    color: white
    display: flex
    justify-content: space-between
    align-items: center
    letter-spacing: 0.05em
    box-shadow: 1px 1px 5px 1px rgba(0,0,0,0.5)
    z-index: 10
    flex-shrink: 0

    .topbar-side
        display: flex
        align-items: center
        height: 100%
        // margin-right: 20px
        #bsslogo
            margin-left: 20px
            img
                height: 40px
                width: 40px
                margin-right: 10px
        #title
            font-weight: 800
            margin-right: 30px

    .topline-button
        padding-left: 20px
        padding-right: 20px
        height: 100%
        color: white
        text-decoration: none
        display: flex
        align-items: center
        &.router-link-active
            background-color: rgba(255,255,255,0.1)
        &:hover
            cursor: pointer
            background-color: rgba(0,0,0,0.1)

    #user
        position: relative
        height: 100%
        padding-left: 20px
        padding-right: 30px
        display: flex
        align-items: center
        margin-left: auto
        // margin-right: 10px
        #usericon
            display: flex
            align-items: center
        #username
            margin-left: 15px
        &:hover
            cursor: pointer
            background-color: rgba(0,0,0,0.1)

    #user-dropdown
        display: none
        z-index: 1
        position: absolute
        top: 60px
        right: 0
        left: 0
        background-color: #2C9DD1
        flex-direction: column

        #user-dropdown-item
            height: 60px
            padding: 10px
            padding-right: 30px
            display: flex
            justify-content: flex-end
            align-items: center
            &:hover
                cursor: pointer
                background-color: rgba(0,0,0,0.1)

    #user:hover > #user-dropdown
        display: flex

</style>
