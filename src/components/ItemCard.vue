<template>
  <v-col class="col-md-3">
  <v-card elevation="2" outlined class="pa-4" tile height="500">

    <v-img :src="ItemImage" :width="250">
    </v-img>
    <v-card-subtitle class="text-wrap">
      {{ ItemName }}
    <br><br>
    <span style="color:green">${{ ItemPrice }}</span>
    </v-card-subtitle>

    <v-btn
      v-on:click="addItemToCart( ItemName, ItemPrice, ItemImage ), showDialog=true" class="ml-3">
    ADD TO CART
    </v-btn>

    <v-dialog v-model="showDialog" width="500">
        <v-card>
          <v-card-text class="shop bold pt-8 black--text" align="center">
            Item Added to Cart
          </v-card-text>
          <v-card-text class="body" align="center">
            <b>{{ ItemName }}</b> has been added to your cart.
          </v-card-text>
          <v-card-actions class="body pb-8" align="center">
            <v-spacer></v-spacer>
            <v-btn @click="showDialog = false">
              Continue Shopping
            </v-btn>
            <v-col cols="1"></v-col>
            <v-btn @click="proceedToCart">
              View Cart
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

  </v-card>
</v-col>
</template>

<script>
// import {mapActions, mapGetters} from 'vuex'

export default {
    name: "ItemCard",
    props: {
      ItemImage: String,
      ItemName: String,
      ItemPrice: Number,
      // ItemID: Number
    },
    data() {
      return {
        showDialog: false
      }
    },
    methods: {
      addItemToCart: function(ItemName, ItemPrice,ItemImage) {
        this.$store.dispatch('addItemToCart', {ItemName, ItemPrice, ItemImage})
      },
      proceedToCart: function() {
      this.$router.push('/ShoppingCart')
    },
    }
}
</script>
