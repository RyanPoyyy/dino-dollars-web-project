// import axios from "axios";

export async function callASOS(){
    try{
        const axios = require('axios')
        const graphqlurl="http://localhost:5030/graphql"
        const graphqlQuery = {
            "operationName": "Query",
            "query": `query Query { items { name price imageUrl } }`
            
        };


        const response=  await axios({url:graphqlurl, method:'post', data:graphqlQuery})
        let items_list= response.data.data.items;
        items_list= items_list.map(function(item){
            const temp= {
                name:item.name,
                price: item.price,
                imageUrl: "http://" + item.imageUrl
            }
            return temp
        })
        console.log(items_list)
        return items_list
    }
    catch (err){
        console.log(err)
    }
}