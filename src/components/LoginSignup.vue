<template>
  <v-app id="inspire">
    <v-content class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #95C4CB, #214F84)', minHeight: '100vh' }">
      <v-container class="fill-height" fluid align="center" justify="center">
        <v-row align="center" justify="center">
          <v-col cols="12" md="4">
            <v-card class="elevation-10 rounded-xl" align="center" justify="center">
                  <v-col cols="10" md="8" align="center" justify="center">
                  <v-row align="center" justify="center">
                    <img src="../assets/dinodollar logo transparent.png" height="200" align="center" justify="center">
                  </v-row>
                  <v-row></v-row>
                  
                  <v-row class="header green--text" align="center" justify="center">
                    Start earning Dino Dollars today!
                  </v-row><br><br>
                  <v-row class="btn" align="center" justify="center">
                    <router-link to="/LoginPage" tag="v-btn">
                    <v-btn class="btn white--text mx-4" color="green darken-2">Login</v-btn>
                  </router-link>
                  <router-link to="/SignupPage" tag="v-btn">
                    <v-btn class="btn white--text mx-4" color="green darken-2">Sign Up</v-btn>
                  </router-link>
                  </v-row>
                  <br>
                  </v-col>
            </v-card>
          </v-col>
          </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<style>
h1, .header {
  font-family: brightwall;
  font-weight: bold;
  font-size:20px
}

h2, .body, .btn {
  font-family: glacial_bold;
}

h3, .body {
  font-family: glacial;
}
</style>



