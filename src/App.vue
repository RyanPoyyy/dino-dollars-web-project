<template>
  <v-app>

    <v-main>


    <!-- <AsosUI/> -->

    <!-- <NavBar/> -->
    
    <router-view></router-view>

    <!-- For Rapie's testing -->
    <!-- <Axiostest/> -->
    </v-main>
  </v-app>
</template>

<script>
// import AsosUI from  './components/AsosWebsite.vue';
// import Axiostest from './components/axios-testing.vue'

export default {
  name: 'App',

  components: {
    // AsosUI
  },

  data() {
    return {
      // asos: true
    };
  }
};
</script>
