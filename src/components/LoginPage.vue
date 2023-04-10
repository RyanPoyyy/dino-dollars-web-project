<template>
  <v-app id="inspire">
    <v-content class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #95C4CB, #214F84)', minHeight: '100vh' }">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="8" md="6">
            <v-card class="elevation-10 rounded-xl" align="center" justify="center">                                  
                <v-col cols="10" align="center" justify="center">
                    <v-card-text class="mt-12">

                    <!-- Error tag -->
                    <div v-if="error">
                        <v-alert type="error">
                            {{ error }}
                        </v-alert>
                    </div>
                
                <h1 class="text-center header green--text text--darken-2">Login to Dino Dollars</h1><br>
                <h4 class="text-center">Enter your email and password!</h4>

                <img src="../assets/dinodollar logo transparent.png" height="200" align="center" justify="center">

                    
                    <v-form class="body">
                        <v-text-field v-model="email"
                        label="Email"
                        name="Email"
                        type="email"
                        color="teal accent-3"
                        />

                        <v-text-field v-model="password"
                        id="password"
                        label="Password"
                        name="password"
                        
                        type="password"
                        color="teal accent-3"
                        />
                    </v-form>
                    </v-card-text>

                    <div class="text-center mt-3">
                    <v-btn class="btn white--text" color="green darken-2" type="submit" :disabled="!signInValid" @click="logIn" >SIGN IN</v-btn>
                    </div><br>
                    
                    <div class="body">
                        Don't have an account? Sign up <router-link to="/SignupPage" class="green--text">here</router-link>!
                    </div><br>
                </v-col>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    step: 1,
    email:'',
    password:'',

    error:false,
  }),

  computed:{
    signInValid(){
      return this.email!='' && this.password!='' 
    },

    signUpValid(){
      return this.email!='' && this.password!=''&& this.name!='' 
    },
    user(){
      return this.$store.getters.getUser
    }
  },

  watch:{
    user(value){
      if(value!=null && value!=undefined){
        this.$router.push('/')
      }
    }
  },

  methods:{

    stepper(){
      this.error=false
      if(this.step==2){
        this.step=1
      }
      else{
        this.step=2
      }
    },

    logIn(){
      this.error=false
      let payload={
        'email':this.email,
        'password':this.password
      }
      this.$store.dispatch("signUserIn", payload)
      .then( (res)=>{
        if(res.status!=='success'){
          console.log(res)
        this.error=res.message
        }
      })
    //   catch((err)=>{
    //     console.log(err)
    //     this.error=err.message
    //   })
      
    },


    signUp(){
      this.error=false
      let payload={
        'Name':this.name,
        'Email':this.email,
        'Password':this.password
      }

      // committing to signup action:
      let url="http://127.0.0.1:5003/user"
      axios.post(url, payload)
      .then((response)=>{
        console.log(response)
        this.name=''
        this.email=''
        this.password=''
        this.$router.go()
      })
      .catch( (err)=>{
        console.log(err)
        this.error=err.response.data.message
      })
    }
  },

  props: {
    source: String
  }
};
</script>

<style>
h1, .header {
  font-family: brightwall;
}

h2, .body, .btn {
  font-family: glacial_bold;
}

h3, .body {
  font-family: glacial;
}
</style>



