<template>
    <v-app id="inspire">
      <NavBar/>
  
      <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #95C4CB, #214F84)', minHeight: '100vh' }" >
        <v-container>
          <v-row>
            <v-col class="col-2"></v-col>
            <v-col align="center" justify="center">
              <h1 class="green--text text--darken-3">Dino Dollars</h1>
              <br>
              <h2 class="font-weight-medium">SPEND. REDEEM. SAVE.</h2>
              <h3 class="font-weight-light">Dino Dollars rewards vouchers for purchases and helps you save with every dollar spent!</h3>
              <br>
              <v-btn size="small" class="btn white--text" color="green darken-2" @click="scrollToBottom">Earn Dino Dollars Now!</v-btn>
            </v-col>
            
            <v-col align="center" justify="center">
              <!-- change image -->
              <img src="../assets/dinodollar logo transparent.png" height="200">
            </v-col>
            <v-col class="col-2"></v-col>

          </v-row>
          
          <br><br>
          <v-divider color="white"></v-divider>
          <br><br>

          <!-- carousel of partners -->

          <v-div align="center" justify="center">
            <h1 class="font-weight-bold white--text">Earn Dino Dollars with our Partners!</h1><br>

            <v-carousel hide-delimiters v-model="model" width="300" height="320" align="center">
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition">
                <router-link to="/AsosVouchers">
                  <v-img src="../assets/asos.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
                </router-link>

              </v-carousel-item>

              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/adidas.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/nike.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/apple.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
              <v-carousel-item reverse-transition="fade-transition" transition="fade-transition" align-center justify>
                <v-img src="../assets/puma.jpg" width="300" height="300" justify="center" align="center" class="rounded-xl elevation-5"></v-img>
              </v-carousel-item>
            </v-carousel>
          </v-div>

          <br><br>
          <v-divider color="white"></v-divider>
          <br><br>

          <!-- Instructions -->

          <v-div ref="bottom">
            <h1 font-weight-medium align="center" class="white--text">How to earn Dino Dollars?</h1><br><br>

            <v-row align="left" class="pl-8 mx-8">
              <!-- <v-col class="col-3"> -->
                <v-card width="500" class="rounded-xl" color="#388E3C">
                  <v-card-title class="justify-left header white--text">Link</v-card-title>
                  <v-card-text class="body white--text">Connect your Dino Dollars account with our partner companies to get started.</v-card-text>
                </v-card>
              <!-- </v-col> -->
              <v-spacer></v-spacer>
              <img src="../assets/Link.png" height="100">
              <img src="../assets/Link.png" height="100">
              <img src="../assets/Link.png" height="100">
              <img src="../assets/Link.png" height="100">
              <img src="../assets/Link.png" height="100">
              <img src="../assets/Link.png" height="100">

            </v-row>
            <br><br><br>

            <v-row align="right" class="pr-2 mx-8">
            <img src="../assets/Spend.png" height="100">
            <img src="../assets/Spend.png" height="100">
            <img src="../assets/Spend.png" height="100">
            <img src="../assets/Spend.png" height="100">
            <img src="../assets/Spend.png" height="100">
            <img src="../assets/Spend.png" height="100">
            <v-spacer></v-spacer>
              <!-- <v-col align="right" class="pr-10 mx-2"> -->
                <v-card align="right" width="500" class="rounded-xl" color="#388E3C">
                  <v-card-title class="justify-left header white--text">Spend</v-card-title>
                  <v-card-text align="left" class="body white--text">Make a purchase from one of our partner companies and receive Dino Dollars for every dollar spent. $1 = 10 Dino Dollars!</v-card-text>
                </v-card>
              <!-- </v-col> -->
            </v-row>
            <br><br><br>

            <v-row align="left" class="pl-8 mx-8">
              <!-- <v-col class="col-3"> -->
                <v-card width="500" class="rounded-xl" color="#388E3C">
                  <v-card-title class="justify-left header white--text">Redeem</v-card-title>
                  <v-card-text class="body white--text">Choose from a wide range of Dino vouchers from your favourite brands and redeem them using your Dino Dollars.</v-card-text>
                </v-card>
                <v-spacer></v-spacer>
            <img src="../assets/Redeem.png" height="100">
            <img src="../assets/Redeem.png" height="100">
            <img src="../assets/Redeem.png" height="100">
            <img src="../assets/Redeem.png" height="100">
            <img src="../assets/Redeem.png" height="100">
            <img src="../assets/Redeem.png" height="100">

              <!-- </v-col> -->
            </v-row>
            <br><br><br>

            <v-row align="right" class="pr-2 mx-8">
            <img src="../assets/Save.png" height="100">
            <img src="../assets/Save.png" height="100">
            <img src="../assets/Save.png" height="100">
            <img src="../assets/Save.png" height="100">

            <v-spacer></v-spacer>
              <!-- <v-col align="right" class="pr-10 mx-2"> -->
                <v-card width="500" class="rounded-xl" color="#388E3C">
                  <v-card-title class="justify-left header white--text">Save</v-card-title>
                  <v-card-text align="left" class="body white--text">Use Dino vouchers to save money on your purchases and enjoy exclusive discounts that you won't find anywhere else.</v-card-text>
                </v-card>
              <!-- </v-col> -->
            </v-row>
            <br>
            
            <!-- <v-row>
              <v-col class="col-3">
                <v-card height="180" class="rounded-xl">
                  <v-card-title class="justify-center header">Save</v-card-title>
                  <v-card-text class="body">Use Dino vouchers to save money on your purchases and enjoy exclusive discounts that you won't find anywhere else.</v-card-text>
                </v-card>
              </v-col>
            </v-row> -->
            
          </v-div>
          
        </v-container>
  
      </v-main>
    </v-app>
  </template>

<script>
import NavBar from './NavBar.vue'
// import axios from 'axios'

export default {
  components: {
    NavBar
  },
  data () {
    return {
      partners: [
        {name: 'Asos', src:'../assets/asos.jpg'},
        {name: 'Adidas', src:'../assets/adidas.jpg'},
        {name: 'Nike', src:'../assets/nike.jpg'},
        {name: 'Apple', src:'../assets/apple.jpg'},
        {name: 'Puma', src:'../assets/puma.jpg'},
      ],
    }
  },

  methods: {
    scrollToBottom(){
      this.$refs['bottom'].scrollIntoView({behavior: "smooth"})
    }  
  }
}

</script>

<style>
h1, .header {
  font-family: brightwall;
}

h2, .body, .heading {
  font-family: glacial_bold;
}

h3, h4, .body {
  font-family: glacial;
}
</style>
