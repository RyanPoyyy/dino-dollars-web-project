<template>
    <v-card class="rounded-lg" outlined>
        <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title class="shop mb-1" >{{ voucher_obj.DiscountAmt }}% off</v-list-item-title>
            <v-list-item-title class="body">{{ voucher_obj.DDRequired }} points</v-list-item-title>
            <v-list-item-subtitle class="body">{{ voucher_obj.Platform_Name }} voucher</v-list-item-subtitle>
        </v-list-item-content>

        <unavailableButton/>
        
        <!-- <v-btn class="rounded-lg" color="primary" outlined text>Purchase</v-btn> -->
        </v-list-item>
    </v-card>
</template>

<script>
import unavailableButton from './unavailable_voucher_button.vue';

export default {
    props:['voucher_obj']
    
    ,

    components: {
        unavailableButton
    },
    data() {
        return {
            drawer: false
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