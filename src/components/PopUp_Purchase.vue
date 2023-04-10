<template>
    <v-row class="mx-1">
      <v-spacer></v-spacer>
      <v-btn color="primary" class="rounded-lg shop" outlined text @click.stop="dialog = true">
        PURCHASE
      </v-btn>
  
      <v-dialog v-model="dialog" max-width="290">
        <v-card class="px-5 pt-5 pb-5 mx-auto text-center d-inline-block shop" variant="outlined">
          <v-card-title class="shop text-center" style="word-break: break-word">
            Purchase this voucher?
          </v-card-title>
  
          <v-card-actions class="d-flex align-center justify-center">
            <v-btn color="grey lighten-3" class="ma-1" @click="dialog = false">
              Cancel</v-btn>
  
            <v-btn color="green lighten-2" class="ma-1" light @click="buyVoucher(); dialog = false">
              Yes</v-btn> 

            <!-- <v-btn color="blue lighten-2" class="ma-1" light @click="buyVoucher()">
            Testing</v-btn>  -->
            <!-- link to my vouchers page and display newly bought voucher -->
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
import axios from "axios";

export default {
  data () {
    return {
      dialog: false,
    }
  },
  props: 
    ['voucher_obj']
  ,
  methods: {
    // how to pass in the DDRequired and all these 
    // {
    // "pname": "ASOS",
    // "discount": "5% Discount",
    // "uid": 2,
    // "DDRequired": 20
    // }

    buyVoucher() {
      let userObj=this.$store.getters.getUser
      let userUID = userObj.UID
      let platformName = this.voucher_obj.Platform_Name
      let discountAmt = this.voucher_obj.DiscountAmt
      let ddRequired = this.voucher_obj.DDRequired

      let url = "http://localhost:6002/buy_voucher/" + userUID + "/" + ddRequired

      console.log(url)

      let body = {
        "pname": platformName,
        "discount": discountAmt,
        "uid": userUID,
        "DDRequired": ddRequired
      }

      axios.post(url, body)
      .then(response => {
        console.log(response)
        this.$router.push('/MyVouchers')
      })
      .catch(error => {
        console.log(error)
      })
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