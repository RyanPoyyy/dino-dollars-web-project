<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #214F84, #95C4CB)', minHeight: '100vh' }" >

        <NavBar/>

            <v-container align="center" class="white--text">

                <v-div align="center">
                    <h1>My Available Vouchers</h1>
                </v-div><br>

                <v-div>
                    <v-responsive>
                    <v-text-field dense flat hide-details rounded label="Search for categories or stores" height="50" class="white"></v-text-field>
                    </v-responsive>
                </v-div><br><br>

            <v-row>
            <v-col>
                <v-div>
                    <h2>Available Vouchers:</h2><br>
                    <!-- implement code to determine number of vouchers to display -->
                    <!-- <Voucher_ShopNow/><br>
                    <Voucher_ShopNow/><br>
                    <Voucher_ShopNow/> -->

                    <div v-for="(voucher,index) in this.my_vouchers" v-bind:key="index">
                    <Voucher_ShopNow
                v-bind:voucher_obj="voucher"
                 /><br></div>
                </v-div>
            </v-col>
            </v-row>

     
            </v-container>            

        </v-main>
    </v-app>

</template>

<script>
import Voucher_ShopNow from './Voucher_ShopNow.vue'
import NavBar from './NavBar.vue'
import axios from 'axios'

export default {
  name: 'MyVouchers',

  components: {
    NavBar,
    Voucher_ShopNow,
  },

  data () {
    return {
        my_vouchers: [],
        UID: null
    }
  },

  created() {
    let userObj=this.$store.getters.getUser
        this.UID=userObj.UID
        let url="http://127.0.0.1:5002/purchasedvoucher"+'/'+this.UID
        axios.get(url)
        .then( (response)=>{
            console.log(response)
            this.my_vouchers=response.data.data.AllVouchers
            console.log(this.my_vouchers)
        })
        .catch((err)=>{
            console.log(err)
        })
  }
};
</script>