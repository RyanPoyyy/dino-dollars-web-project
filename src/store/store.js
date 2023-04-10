import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        cart: [
        ],
        amount: 0,
        discountedAmount: null,
        // pointsEarned: null,
        voucher: null,
        user: null,
        
    },
    getters: {
        // somethingChanged: state => {
        //     var somethingChange = state.cart.map( something => {
        //         return {
        //           name: '**' + something.name + "**"
        //         }
        //       });
        
        //       return somethingChange
        // }
        // cartTotal: state => {
        //     state.cart.forEach(item => {
        //         state.amount += item.price
        //     })

        //     // return state.amount
        // },

        // getCart: state => {
        //     return state.amount
        // },

        //returning the vuex user state, can be seen in the console log.
        getUser(state){
            console.log(state.user)
            return state.user
        },
        getVoucher(state){
            return state.voucher
        }
    },
    mutations: {
        // changeName: state => {
        //     state.cart.forEach(something => {
        //         something.name = something.name + "&&&"
        //     })
        // },
        addItemToCart: (state,payload) => {
            state.cart.push({name: payload.ItemName, price:payload.ItemPrice, ItemImage:payload.ItemImage})
            state.amount += payload.ItemPrice
            state.discountedAmount += payload.ItemPrice
        },
        removeAllItems: state => {
            state.cart = []
            state.amount = 0
            state.discountedAmount = null
            state.voucher = null
        },
        // removeItem: (state,payload) => {
        //     item.find()
        // }
        // checkoutCart: state => {
        //     state.cart.forEach(item => {
        //         state.amount += item.price
        //     })
        // }

        applyVoucher: (state,payload) => {
            state.voucher = payload
        },
        // removeVoucher: state => {
        //     state.voucher = null
        // },
        logUser (state, payload){
            state.user=payload
        },

        logOut (state){
            state.user=null
        },
        setUserStatePoints(state,payload) {
            state.user.Points = payload
        }

        
    },
    actions: {
        // changeName: context => {
        //     setTimeout(function(){
        //         context.commit('changeName')
        //     }, 2000)
        // },
        addItemToCart: (context,payload) => {
            context.commit('addItemToCart', payload)
        },
        removeAllItems: context => {
            context.commit('removeAllItems')
        },
        removeVoucher: context => {
            context.commit('removeVoucher')
        },
        // removeItem: (context,payload) => {
        //     context.commit('removeItem',payload)
        // }
        // checkoutCart: context => {
        //     context.commit('checkoutCart')
        // },

        pointsUpdate: (context) => {
            axios.put('http://127.0.0.1:5003/point/1', {
                Points:  context.state.amount
            })
            .then(response => {
                console.log(response.data)
            })
            .catch( error => {
                console.log(error.message);
            });
        },
        setUserStatePoints: (context,payload) => {
            context.commit("setUserStatePoints",payload )
        },
        applyVoucher: (context,payload) => {
            context.commit('applyVoucher',payload)
        },
        signUserIn( {commit}, payload){
            let email=payload.email
            let password=payload.password
            let url="http://127.0.0.1:5003/user/"+ email+'/'+password 
            return axios.get(url, payload)
            .then(response => {
                //if user logs in
                console.log(response.data)
                const loggedUser= response.data.data
                commit('logUser',loggedUser)

            })
            .catch( error => {
                // if user fails to log in
                // console.log(error)
                console.log(error.response.data);
                return error.response.data

            });
         
        },

        logUserOut( {commit}){
            commit('logOut')
        }
    },
}
);