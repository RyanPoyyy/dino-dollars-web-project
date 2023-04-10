<template>
    <v-app id="inspire">
        <NavBar/>
        <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #214F84, #95C4CB)', minHeight: '100vh' }" >
            <v-container align="center">
                <v-div align="center" class="white--text">
                    <h1>Our Partners</h1><br>
                    <h3 class="font-weight-light">Dino Dollars is here to help you save while shopping online! With more than 100 trusted partners, we offer exclusive deals for all users to earn rewards on their purchases.<br>

                    Whether you're a seasoned online shopper or just getting started, there's something for everyone. From fashion and beauty to electronics and groceries, we have a wide range of categories to choose from. Purchase any voucher of your choice, and start accumulating discounts for all your online shopping needs today!
                    </h3>
                </v-div><br><br>

                <!-- <v-div>
                    <v-responsive>
                    <v-text-field dense flat hide-details rounded solo-inverted label="Search for categories or stores" height="50"></v-text-field>
                    </v-responsive>
                </v-div><br><br> -->

                <v-div>
                    <v-row class="justify-space-between">
                    <v-card width="200" height="200" align="center" class="rounded-xl">
                        <router-link to="/AsosVouchers">
                            <img src="../assets/asos.jpg" width="200" height="200" justify="center" align="center" class="rounded-xl elevation-5">
                        </router-link>
                    </v-card>

                    <v-card width="200" height="200" justify="center" align="center" class="rounded-xl">
                        <img src="../assets/adidas.jpg" width="200" height="200" justify="center" align="center" class="rounded-xl elevation-5">
                    </v-card>

                    <v-card width="200" height="200" justify="center" align="center" class="rounded-xl">
                        <img src="../assets/puma.jpg" width="200" height="200" justify="center" align="center" class="rounded-xl elevation-5">
                    </v-card>

                    <v-card width="200" height="200" justify="center" align="center" class="rounded-xl">
                        <img src="../assets/nike.jpg" width="200" height="200" justify="center" align="center" class="rounded-xl elevation-5">
                    </v-card>

                    <v-card width="200" height="200" justify="center" align="center" class="rounded-xl">
                        <img src="../assets/apple.jpg" width="200" height="200" justify="center" align="center" class="rounded-xl elevation-5">
                    </v-card>
                    </v-row>

                </v-div>



     
            </v-container>
            

        </v-main>
    </v-app>

</template>

<script>
import NavBar from './NavBar'

export default {
  name: 'App',

  components: {
    NavBar,
  }
};
</script>
