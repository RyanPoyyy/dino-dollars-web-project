import {store} from './store.js'
export default(to,from,next)=>{
    if(store.getters.getUser){
        next()
    }
    else{
        next('/LoginSignup')
    }
}