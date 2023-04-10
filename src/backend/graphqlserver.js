const express = require('express')
const axios= require('axios')
const cors= require('cors')
const expressGraphQL= require('express-graphql').graphqlHTTP
const {GraphQLSchema, 
    GraphQLObjectType, 
    GraphQLString,
    GraphQLInt,
    GraphQLFloat,
    GraphQLBoolean,
GraphQLList} = require('graphql')



//connecting to ASOS API and pulling data:



const parameters={
    method: "GET",
url: "https://asos2.p.rapidapi.com/products/v2/list",
params: {
store: "US",
offset: "0",
categoryId: "4209",
limit: "40",
country: "US",
sort: "freshness",
currency: "USD",
sizeSchema: "US",
lang: "en-US",
},
headers: {
"X-RapidAPI-Key": "e2131ac1c7mshf037e692363d1d8p1e89cajsn50d1e5e1a4e6",
"X-RapidAPI-Host": "asos2.p.rapidapi.com",
},
}
axios.request(parameters)
.then( (response)=>{
    items_list=response.data.products
    items_list=items_list.map(function(item){
        const temp={
            id: item.id,
            name:item.name,
            price:item.price.current.value,
            color: item.color,
            brandName: item.brandName,
            isSellingFast: item.isSellingFast,
            url: item.url,
            imageUrl: item.imageUrl,

        }

        return temp
    })

    console.log(items_list)
})
.catch((err)=>{
    console.log(err)
})



//creating express app
const app=express()
app.use(cors())


//creating item type:
const itemType= new GraphQLObjectType({
    name:"item",
    description: "Single Item info",
    fields: ()=>({
        id: {type: GraphQLInt},
        name: {type: GraphQLString},
        price: {type: GraphQLFloat},
        color: {type: GraphQLString},
        brandName: {type: GraphQLString},
        isSellingFast: {type: GraphQLBoolean},
        url: {type: GraphQLString},
        imageUrl: {type: GraphQLString}
    })
})

// creating schema
const RootQueryType = new GraphQLObjectType({
    name: "Query",
    description: "Root Query",
    fields:()=>({
        items:{
            type: new GraphQLList(itemType),
            description: "List of items",
            resolve: ()=> items_list
        }
    })
})
const schema= new GraphQLSchema({
    query: RootQueryType
})

app.use( '/graphql', expressGraphQL({
    schema: schema,
    graphiql: true
}))

app.listen(5030, ()=>{console.log("GraphQL Server running on port 5030")})
