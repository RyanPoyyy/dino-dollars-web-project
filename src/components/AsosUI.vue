<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col v-for="n in 12" :key="n" cols="4">
          <ItemCard
            item-name="testing"
            :item-price=10
          />
        </v-col>
      </v-row>

      <!-- <v-row>
        <v-col v-for="thing in somethingChanged" :key="thing" cols="4">
          {{ thing.name }}
        </v-col>
      </v-row> -->

      <!-- <v-btn v-on:click="changeName">Change Name</v-btn> -->
      <v-btn router to="/ShoppingCart">To the Cart</v-btn>
      
    </v-container>
  </v-app>
</template>

<script>
import ItemCard from "@/components/ItemCard.vue";
import {mapActions, mapGetters} from 'vuex'

export default {
  name: "AsosUI",
  components: {
    ItemCard,
  },
  computed: {
    // something() {
    //   return this.$store.state.cart
    // },
    // somethingChanged(){
    //   return this.$store.getters.somethingChanged
    // }
    ...mapGetters([
      'somethingChanged'
    ])
  },
  methods: {
    // changeName: function() {
    //   // this.$store.state.cart.forEach(something => {
    //   //   something.name = something.name + "&&&"
    //   // })

    //   this.$store.dispatch('changeName')
    // }
    ...mapActions([
      'changeName'
    ])
  }
};
</script>
