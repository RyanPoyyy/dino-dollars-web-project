<template>
    <v-row class="mx-1">
      <v-spacer></v-spacer>
      <v-btn color="primary"  class="rounded-lg shop" outlined text disabled>
        Purchase
      </v-btn>
<!--   
      <v-dialog v-model="dialog" max-width="290">
        <v-card class="px-5 pt-5 pb-5 mx-auto text-center d-inline-block" variant="outlined">
          <v-card-title class="text-h5 text-center" style="word-break: break-word">
            Purchase this voucher?
          </v-card-title>
  
          <v-card-actions class="d-flex align-center justify-center">
            <v-btn color="grey lighten-3" class="ma-1" @click="dialog = false">
              Cancel</v-btn>
  
            <v-btn color="blue lighten-2" class="ma-1" light @click="dialog = false" router to="/MyVouchers">
              Yes</v-btn> 
             link to my vouchers page and display newly bought voucher -->
          <!-- </v-card-actions>
        </v-card>
      </v-dialog> --> 
    </v-row>
</template>

<script>


export default {
//   data () {
//     runavailable_voucher_buttoneturn {
//       dialog: false,
//     }
//   },
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