<template>
  <v-app class="font">
    <v-app-bar app color="black" max-height="200" :style="{ background:grey}" class="font">
      <router-link to="/AsosWebsite">
          <v-avatar class="mr-8" size="60"><img src="../assets/asos.jpg"></v-avatar>
      </router-link>
      <v-responsive align="center" justify="center" class="mr-4">
      <v-text-field dense flat hide-details rounded solo-inverted label="Search for Categories or Items" background-color="white"></v-text-field>
      </v-responsive>

      <router-link to="/ShoppingCart"><v-icon color="white">mdi-cart-outline</v-icon></router-link>
    </v-app-bar>

    <v-main v-if="cartItems.length == 0">
        <v-container>
            <v-row align="center" justify="center">
                <v-icon color="black">mdi-basket-fill</v-icon>
            </v-row>
            <v-row align="center" justify="center" >
                Your cart is empty.
            </v-row>
            <v-row align="center" justify="center" >
                <v-btn router to="/AsosWebsite">Start shopping!</v-btn>
            </v-row><br><br>
            <v-row align="center" justify="center" >
                Connnect to Dino Dollars to redeem vouchers!
            </v-row>
            <v-row align="center" justify="center" >
                <v-btn :to="{name: 'LoginSignup'}">Link my Dino Dollars account</v-btn>
            </v-row>
        </v-container>
    </v-main>

    <v-main v-else grid-list-md>
      <v-row>
        <v-col class="col-1"></v-col>
        <v-col align="center">
          <v-row>
            <b id="heading" class="mb-2">MY BAG</b>
          </v-row><br>

        <v-row v-for="item in cartItems" :key="item.name" class="pb-4">
          
            <v-card width="570">
              <v-row>
              <v-col class="ml-3">
                <v-img :src="item.ItemImage" :width="100" :height="150" contain align="left"></v-img>
              </v-col>
              <v-col align="left" cols="8">
                <v-card-text class="mt-2" align="left" style="font-size:25px; color:green; font-weight: bold;">SGD ${{ item.price }}</v-card-text>
                <v-card-text style="font-size:18px" class="justify-left">{{ item.name }}</v-card-text>
              </v-col>
              <v-spacer></v-spacer>
              </v-row>
            </v-card>
            <v-row></v-row>
        </v-row>

        <v-row>
          <v-btn v-on:click="removeAllItems">Clear Cart</v-btn>
        </v-row><br>
      </v-col>
      <v-col>
        <v-card width="500">
          <v-card-title id="heading"><b>TOTAL</b></v-card-title>
          <v-divider></v-divider>
          <v-card-text><b>Sub-total:</b><span align="right" justify="right"> ${{ cartTotal }}</span> <br>
          <b>Delivery:</b> $0.00</v-card-text>
          <v-divider></v-divider><br>
          <v-row align="center" justify="center">
            <v-btn v-on:click="checkoutCart(); redeemVoucher()" large depressed width="450px" class="btn white--text" color="green darken-2">Checkout</v-btn>
          </v-row><br>
          <v-divider></v-divider>
          <v-card-text><b>WE ACCEPT:</b>
            <v-img src="../assets/paymentmethod.png"></v-img>
          </v-card-text>
        </v-card><br><br>

        <v-card width="500">
          <v-card-title id="heading"><b>MY VOUCHERS</b></v-card-title>
          <v-divider></v-divider>
          <div v-for="(voucher,index) in this.voucher_list" v-bind:key="index">
          <User_Voucher
          v-bind:voucher_obj="voucher"
          />
          </div>
        </v-card>
      </v-col>

      </v-row>
      
    </v-main>

  </v-app>
</template>

<script>
import axios from "axios";
import User_Voucher from "./User_Voucher.vue";

export default {
  name: "ShoppingCart",
  data: () => ({
    token: "",
    voucher_list:[]
  }),
  created(){
    let userObj=this.$store.getters.getUser
    let userUID=userObj.UID
    let url="http://localhost:5002/purchasedvoucher/" + userUID

    axios.get(url)
    .then(response => {
      let allVoucherList = response.data.data.AllVouchers

      for (let i = 0; i < allVoucherList.length; i++) {
        if (!allVoucherList[i].RedeemedDate) {
          this.voucher_list.push(allVoucherList[i])
        }
      }

      console.log(this.voucher_list)
    })
    .catch(err => {
      console.log(err)
    })
  },
  components: {
    User_Voucher,
  },
  computed: {
    cartItems() {
      return this.$store.state.cart;
    },
    cartTotal() {
      let state = this.$store.state
      var amount = 0

      amount = state.amount
      state.discountedAmount = amount

      if (this.$store.state.voucher) {
        let voucherObj=this.$store.getters.getVoucher
        amount = state.amount - ((state.amount/100) * voucherObj.DiscountAmt)
        state.discountedAmount = amount
      }

      return amount.toFixed(2)
    },
  },
  methods: {
    removeAllItems: function () {
      this.$store.dispatch("removeAllItems");
    },
    pointsUpdate: function () {
      this.$store.dispatch("pointsUpdate");
    },
    currentUser() {
      return this.$store.getters.getUser;
    },
    checkoutCart: function () {
      // this.$store.dispatch('paypalTest')
      let authToken = "Bearer " + this.token
      let value = this.cartTotal
      
    
      let data = {
          "intent": "CAPTURE",
          "purchase_units": [
              {
                  "amount": {
                      "currency_code": "USD",
                      "value": value
                  }
              }
          ]
      } 

      let config = {
          headers: {
              "Content-Type": "application/json",
              "Prefer": "return=representation",
              "Authorization": authToken
          }
        }

      axios.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', 
          data, config
      )
      .then(response => {
          // console.log(response)
          let amountSpent = response.data.purchase_units[0].amount.value
          this.pointsAccumulation(amountSpent)
          this.$router.push('/PaymentConfirmed')
          // this.$store.dispatch("removeAllItems");
          // this.$store.dispatch("removeVoucher");
      })
      .catch(error => {
          console.log(error)
      })
    },
    async paypalAuth(){
      return axios({
        url: 'https://api.sandbox.paypal.com/v1/oauth2/token',
        method: 'post',
        headers: { 
            'Accept': 'application/json', 
            'Accept-Language': 'en_US',
            'Content-Type':'application/x-www-form-urlencoded',
            'Access-Control-Allow-Origin': '*', 
        },
        data: { 'grant_type':'client_credentials' },
        auth: {
          username: 'AfhfcAANPYIAq90OTmgdpm11kw9wYoiQU635f5NinRCJa5yXRU1f3UaXTTpRYwvpyjrb5fjyiaMkixUp',
          password: 'EFEP1zHTJlER95z51Vu4xUvMgqz3NBaXEYsXRTbxdLcy5ziX4Jt-N1dUMV86dW4t0dxN-WDbMm-m6x8I'
        }
      })
      .then(response => {
        // console.log(response.data.access_token)
        return response.data.access_token
      })
      .catch(error => {
        console.log(error)
      })
    },

    getToken: async function() {
      let response = await this.paypalAuth()
      this.token = response
    },

    pointsAccumulation: function(amountSpent) {
      let currentUser = this.currentUser()
      let currentUID = currentUser.UID
      // let state = this.$store.state
      // console.log(currentUID.UID)

      let url = "http://localhost:6003/add_points/" + currentUID
      let data = {"Points": amountSpent}

      axios.post(url,data)
      .then(response => {
        // console.log("I'm testing something" + response.data.data.Points)
        this.$store.dispatch("setUserStatePoints", response.data.data.Points);
      })
      .catch(error => {
        console.log(error)
      })
    },

    redeemVoucher: function() {
      let vid = this.$store.state.voucher.Vid
      console.log(vid)
      let url = "http://localhost:5010/redeem_voucher/" + vid

      axios.get(url)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  mounted: function() {
    this.getToken();
  }
};
</script>

<style>
.font {
  font-family: glacial;
}

#heading {
  font-size: 25px;
}
</style>