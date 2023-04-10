<template>
    <v-card class="rounded-lg" outlined>
        <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title class="shop mb-1" >{{ discountAmount }}% off</v-list-item-title>
            <v-list-item-title class="body">{{ ddRequired }} points</v-list-item-title>
            <v-list-item-subtitle class="body">{{ expiryDate }}</v-list-item-subtitle>
        </v-list-item-content>

        <v-btn
            elevation="2"
            @click="applyVoucher(voucher_obj)"
        >Apply Voucher</v-btn>
        
        <!-- <v-btn class="rounded-lg" color="primary" outlined text>Purchase</v-btn> -->
        </v-list-item>
    </v-card>
</template>

<script>

export default {
    props:
    {
        'voucher_obj':Object
    },
    components: {
        
    },
    data() {
        return {
            drawer: false,
            asos: false,
            discountAmount:this.voucher_obj.DiscountAmt,
            ddRequired:this.voucher_obj.DDRequired,
            expiryDate:this.voucher_obj.ExpiryDate.slice(4,16),
            vid: this.voucher_obj.Vid
        }
    },
    methods: {
        applyVoucher(voucher_obj) {
            console.log(voucher_obj)
            this.$store.dispatch('applyVoucher', voucher_obj)
        }
    }
}

</script>