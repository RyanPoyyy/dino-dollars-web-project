import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from './components/HomePage.vue'
import BuyVouchers from './components/BuyVouchers.vue'
import MyVouchers from './components/MyVouchers.vue'
import AsosVouchers from './components/AsosVouchers.vue'
import PopUp_Purchase from './components/PopUp_Purchase.vue' 
import PopUp_ShopNow from './components/PopUp_ShopNow.vue' 
import LoginSignup from './components/LoginSignup.vue'
import AsosUI from "./components/AsosUI.vue"
import AsosWebsite from './components/AsosWebsite.vue'
import ShoppingCart from './components/ShoppingCart.vue'
import LoginPage from './components/LoginPage.vue'
import SignupPage from './components/SignupPage.vue'
import PaymentConfirmed from './components/PaymentConfirmed.vue'
import authguard from './store/auth.js'


Vue.use(VueRouter)

export default new VueRouter ({ 
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path:'/',
            name: 'HomePage',
            component: HomePage
        },
        {
            path: '/BuyVouchers',
            name: 'BuyVouchers',
            component: BuyVouchers,
            beforeEnter:authguard,
        },
        {
            path: '/MyVouchers',
            name: 'MyVouchers',
            component: MyVouchers,
            beforeEnter:authguard,
        },
        {
            path: '/AsosVouchers',
            name: 'AsosVouchers',
            component: AsosVouchers,
            beforeEnter:authguard,
        },
        {
            path: '/PopUp_Purchase',
            name: 'PopUp_Purchase',
            component: PopUp_Purchase,
            beforeEnter:authguard,

        },
        {
            path: '/PopUp_ShopNow',
            name: 'PopUp_ShopNow',
            component: PopUp_ShopNow,
            beforeEnter:authguard,

        },
        {
            path: '/LoginSignup',
            name: 'LoginSignup',
            component: LoginSignup
        },
        {
            path: '/AsosUI',
            name: 'AsosUI',
            component: AsosUI,
            beforeEnter:authguard,

        },
        {
            path: '/AsosWebsite',
            name: 'AsosWebsite',
            component: AsosWebsite,
            beforeEnter:authguard,

        },
        {
            path: '/ShoppingCart',
            name: 'ShoppingCart',

            component: ShoppingCart,
            beforeEnter:authguard,

        },
        {
            path: '/LoginPage',
            name: 'LoginPage',
            component: LoginPage,

        },
        {
            path: '/SignupPage',
            name: 'SignupPage',
            component: SignupPage,

        },
        {
            path: '/PaymentConfirmed',
            name: 'PaymentConfirmed',
            component: PaymentConfirmed,

        }
    ]
})