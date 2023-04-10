<template>
    <v-row justify="center">
      <v-btn class="btn white--text" color="green darken-2"  @click.stop="dialog = true"  align="center" justify="center">
        SHOP NOW
      </v-btn>
  
      <v-dialog v-model="dialog" max-width="290">
        <v-card class="px-5 pt-5 pb-5 mx-auto text-center d-inline-block shop" variant="outlined">
          <v-card-title class="text-center" style="word-break: break-word">
            Leave site to shop at ASOS?
          </v-card-title>
  
          <v-card-actions class="d-flex align-center justify-center">
            <v-btn color="grey lighten-3" class="ma-1" @click="dialog = false">
              Cancel</v-btn>
  
            <v-btn color="green lighten-2" class="ma-1" light @click="shopNow" > 
              Yes</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      dialog: false
      
    }
  },

  methods:{
    shopNow(){
      console.log(1)
      this.dialog=true
      let userObj=this.$store.getters.getUser
      let url="http://127.0.0.1:5003/accounts/" + userObj.UID+'/'+"ASOS"
      console.log(url)
      axios.post(url)
      .then((response)=>{
        console.log(response)
      })
      .catch((err)=>{
        console.log(err)
      })
      this.$router.push('/ASOSWebsite')
    }
  }
}
</script>


<style>
.shop {
  font-family: glacial_bold;
}

h3, .body {
  font-family: glacial;
}
</style>