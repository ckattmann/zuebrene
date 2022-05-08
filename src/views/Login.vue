<template lang='pug'>

#login-container
    #login-window
        div#bsslogo
            img#logo(src="../assets/bss-logo.svg")
        input(placeholder='Username', v-model='username', v-on:keyup.enter="login2")
        input(placeholder='Password', type='password', v-model='password', v-on:keyup.enter="login2")
        Button#loginbutton(@click='login2') Login
        div#error-text {{ error_text }}

</template>

<script>

import Vue from 'vue'
import store from '@/store.js'
import axios from 'axios';

export default {
    name: 'Login',
    components: {},
    data: function() {
        return {
            username: '',
            password: '',
            login_status: '',
            error_text: ''
        }
    },
    methods: {
        login2() {
            this.error_text = ''
			this.$store.dispatch('login', {
				username: this.username,
				password: this.password
			}).then(() => {
				// this.$store.dispatch('getDevices');
				this.$router.push('/livedata')
			}).catch(err => {
                this.error_text = 'Login Failed'
				console.log(err)
			})
        },
        // login() {
        //     // OAUTH2 Login Flow:
        //     // username and password need to be packed as form:
        //     let oauth2FormData = new FormData()
        //     oauth2FormData.append('username', this.username)
        //     oauth2FormData.append('password', this.password)
        //     // oauth2FormData MUST be passed as second parameter, {data: oauth2FormData} doesnt work:
        //     // (data must be send as form, not as json)
        //     axios.post('/api/token', oauth2FormData).then((response) => {
        //         console.log(response.data)
        //         this.error_text = ''
        //         this.$router.push('/map')
        //     }).catch((error) => {
        //         console.log(error)
        //         this.error_text = 'Login Failed'
        //         // this.password = ''
        //     })
        // }

    },
    mounted() {
    }
}
</script>

<style lang='sass' scoped>

#logo
    width: 150px
    margin: 20px

#login-container
    width: 100%
    /* height: 1024px; */
    position: absolute
    bottom: 0
    top: 0
    left: 0
    right: 0
    display: flex
    justify-content: center
    align-items: center

#login-window 
    width: 200px
    padding: 30px
    padding-bottom: 10px
    border-radius: 20px
    background-color: whitesmoke
    box-shadow: 1px 1px 5px 1px rgba(0,0,0,0.2)
    display: flex
    flex-direction: column
    align-items: center

    input
        margin-bottom: 10px

    #loginbutton
        width: 100px
        margin-bottom: 10px

    #error-text
        height: 20px
        display: flex
        align-items: center
</style>
