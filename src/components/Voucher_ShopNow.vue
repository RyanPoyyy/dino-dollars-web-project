<template>

    <v-card class="mx-auto rounded-lg" variant="outlined" v-if="redeemedDate==null">

        <v-card-text class="py-0">
            <v-row align="center" gutter>
                <v-col cols="2">
                <v-img src="../assets/asos.jpg" width="100" height="100" justify="centre" align="left" class="rounded-xl elevation-5"></v-img>
                </v-col>

                <v-col cols="8" >
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="shop mb-1" >{{ discountAmount }}% off</v-list-item-title>
                            <v-list-item-title class="body">Cost of Voucher: {{ ddRequired }} points</v-list-item-title>
                            <v-list-item-subtitle class="body">Date of Purchase: {{ purchasedDate }}</v-list-item-subtitle>
                        </v-list-item-content>
                       </v-list-item>
                </v-col>
                
                <v-col cols="1" class="ml-3">
                <PopUp_ShopNow/>
                </v-col>

            </v-row>
        </v-card-text>

        <br/>
        
    </v-card>

    <v-card class="mx-auto rounded-lg" color="grey" variant="outlined" v-else>
        <v-card-text class="py-0">
            <v-row align="center" gutter>
                <v-col cols="2">
                <v-img src="../assets/asos.jpg" width="100" height="100" justify="centre" align="left" class="rounded-xl"></v-img>
                </v-col>

                <v-col cols="8" >
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="shop mb-1" >{{ discountAmount }}% off</v-list-item-title>
                            <v-list-item-title class="body">Cost of Voucher: {{ ddRequired }} points</v-list-item-title>
                            <v-list-item-subtitle class="body">Date of Purchase: {{ purchasedDate }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                
                <v-col cols="2" class="shop">
                REDEEMED
                </v-col>

            </v-row>
        </v-card-text>

<br/>

</v-card>
</template>

<script>
import PopUp_ShopNow from './PopUp_ShopNow.vue';

export default {
    props: {
        'voucher_obj': Object
    },
    components: {
        PopUp_ShopNow 
    },
    data() {
        return {
            drawer: false,
            discountAmount:this.voucher_obj.DiscountAmt,
            ddRequired:this.voucher_obj.DDRequired,
            // expiryDate:this.voucher_obj.ExpiryDate.slice(4,16),
            purchasedDate: this.voucher_obj.PurchasedDate.slice(4,16),
            redeemedDate: this.voucher_obj.RedeemedDate
        }
    },
    created() {
        console.log(this.voucher_obj)
    }
}

</script>

<style>
.shop {
  font-family: glacial_bold;
  font-size: 25px
}

h3, .body {
  font-family: glacial;
}
</style>