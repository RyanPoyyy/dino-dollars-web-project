<template>
    <v-app id="inspire">
        <v-main class="blue lighten-4" :style="{ background: 'linear-gradient(to bottom, #95C4CB, #214F84)', minHeight: '100vh' }" >
            <NavBar/>
            <v-container align="center">
               
            <v-row>
                <v-col class="col-4" rowspan="2">
                <v-card class="rounded-lg py-0 my-0" max-width="300">
                    <v-list-item two-line align="center">
                    <v-list-item-content>
                        <div><img src="https://www.theclimatepledge.com/content/dam/amazonclimatepledge/signatory-logo/ASOS.png" width="200"></div>
                        <v-list-item-title class="font-weight-light slogan">
                        Discover the latest fashion <br>
                        trends with ASOS. Shop the <br>
                        new collection and more!
                        </v-list-item-title><br><br>
                        <div>
                            <PopUp_ShopNow/>
                        </div><br><br><br>
                    </v-list-item-content>
                    </v-list-item>
                </v-card><br>

                <v-card class="rounded-lg py-0" max-width="300">
                    <v-list-item align="center">
                    <v-list-item-content>
                        <v-list-item class="header mb-1 font-weight-medium py-1">
                            Ensure voucher eligibility:
                        </v-list-item>
                        <v-list-item align="left" class="condition">
                            1. Check voucher's expiration date
                        </v-list-item>
                        <v-list-item align="left" class="condition">
                            2. Read the terms and conditions
                        </v-list-item>
                    </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-col>

            <v-col>

                <h1>Your Current DinoDollars : <span id="body">{{ points }}</span></h1>
                <br>
                <h2>Available Vouchers:</h2><br>
                <div v-if="available_voucher_list.length==0">
                    <h4>You have insufficient points to purchase any voucher.</h4>
                </div>
                <!-- implement code to determine number of vouchers to display -->
                <div v-for="(voucher,index) in this.available_voucher_list" v-bind:key="index">
                <Voucher_Purchase 
                v-bind:voucher_obj="voucher"
                 /><br>
                <!-- <Voucher_Purchase/><br>
                <Voucher_Purchase/> -->
            </div>


            <div v-if="unavailable_voucher_list.length!=0">
                <br><br><br>
                <h2>Unavailable Vouchers:</h2><br>
                <div v-if="unavailable_voucher_list!=[]">
                    <h4>Earn more points to purchase these amazing deals!</h4>
                </div><br>
                <!-- implement code to determine number of vouchers to display -->
                <div v-for="(voucher,index) in this.unavailable_voucher_list" v-bind:key="index">
                <Unavailable_Voucher
                v-bind:voucher_obj="voucher"
                 /><br>
                <!-- <Voucher_Purchase/><br>
                <Voucher_Purchase/> -->
            </div>
            
            </div>
            </v-col>
            </v-row>

            <!-- <v-row>


            <v-col v-if="unavailable_voucher_list!=[]">
                <h2>Unavailable Vouchers:</h2><br>
                <div v-if="unavailable_voucher_list!=[]">
                    <h3>Earn more points to purchase these amazing deals!</h3>
                </div>
              implement code to determine number of vouchers to display -->
                <!-- <div v-for="(voucher,index) in this.unavailable_voucher_list" v-bind:key="index">
                <Unavailable_Voucher
                v-bind:voucher_obj="voucher"
                 /><br>
               <Voucher_Purchase/><br>
                <Voucher_Purchase/> 
            </div>
            </v-col>
            </v-row> -->

            
            </v-container>

        </v-main>
    </v-app>

</template>

<script>
import Voucher_Purchase from './Voucher_Purchase.vue'
import Unavailable_Voucher from './unavailable_voucher.vue'
import NavBar from './NavBar'
import PopUp_ShopNow from './PopUp_ShopNow.vue';
import axios from 'axios';


export default {
  name: 'AsosVouchers',

  components: {
    Voucher_Purchase,
    NavBar,
    PopUp_ShopNow,
    Unavailable_Voucher
  },

  data () {
    return {
      asos: false,
      vouchers_list:[],
      available_voucher_list:[],
      unavailable_voucher_list:[],
      UID:null,
      points:0
    }
  },

  created(){
        let userObj=this.$store.getters.getUser
        this.UID=userObj.UID
        let url1="http://127.0.0.1:5003/user/" + this.UID

        axios.get(url1)
        .then( (response)=>{
            console.log(response)
            this.points=response.data.data.Points
        })
        .catch((err)=>{
            console.log(err)
        })
        let url2="http://127.0.0.1:6001/validate_voucher"+'/'+this.UID
        axios.get(url2)
        .then( (response)=>{
            // console.log(response.data)
            // console.log(response.data.data.AllVouchers)
            this.vouchers_list=response.data
            this.available_voucher_list=this.vouchers_list[0]
            this.unavailable_voucher_list=this.vouchers_list[1]
      

            // vouchers_list is in the format of 
            // {
            //     "DDRequired":
            //     DiscountAmt:
            //     PlatformName:
            // }

        })
        .catch((err)=>{
            console.log(err)
        })

        
    
  }
};
</script>


<style>
.header {
  font-family: brightwall;
}

.slogan {
  font-family: glacial;
  font-size: 20px
}

.eligibility {
  font-family: glacial_bold;
}

.condition {
    font-family: glacial;
}

#body {
    font-family: glacial_bold;
    font-size: 30px;
}
</style>