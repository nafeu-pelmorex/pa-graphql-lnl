# Pelmorex Audience - GraphQL Lunch & Learn

Demo project for the GraphQL lunch & learn which took place on March 2019 at Pelmorex LV office.

### Requirements

...

### Setup & Installation

...

### Development

...

### Presentation Info

We want to demonstrate how graphql can be used to replace REST apis (with new Graph API)

**Notes**:

External Microservices:
RecipesAPI => Flask App (Python)
FridgeAPI => Express App (Node.js)

Main App:
MealInquiryAPI => GraphQL API Gateway (Node.js)

**RecipesAPI**

```
data
{
    name: 'Pizza',
    ingredients: ['dough', 'tomato sauce', 'cheese'],
    instructions: [
        'Form dough',
        'Add tomato sauce',
        'Add cheese',
        'Bake in oven for 30 minutes'
    ],
},
{
    name: 'Pasta',
    ingredients: ['pasta', 'tomato sauce', 'cheese'],
    instructions: [
        'Boil pasta',
        'Add tomato sauce',
        'Add cheese',
        'Cook for 15 mins'
    ],
},
{
    name: 'Grilled Cheese',
    ingredients: ['bread', 'cheese', 'butter'],
    instructions: [
        'Put bread in pan with butter',
        'Put cheese inside bread',
        'Heat on pan for 5 minutes'
    ],
},
{
    name: 'Garlic Bread',
    ingredients: ['bread', 'cheese', 'garlic', 'butter'],
    instructions: [
        'Put bread in baking sheet with butter cheese and garlic',
        'Bake in oven for 15 minutes',
    ],
},
```

GET getAll => returns data

**RecipesAPI**

```
data
{
    name: 'dough'
},
{
    name: 'tomato sauce'
},
{
    name: 'cheese'
}
```

GET getAll => returns data

**MealInquiryAPI**

query: {}

**Case**:

...

Questions to Answer:

- What is monolithic architecture?
- What are microservices?
- What are advantages of monolith versus microservices?
https://www.google.ca/imgres?imgurl=https%3A%2F%2Fd1.awsstatic.com%2FDeveloper%2520Marketing%2Fcontainers%2Fmonolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png&imgrefurl=https%3A%2F%2Faws.amazon.com%2Fmicroservices%2F&docid=v5_ybMDNzBRAKM&tbnid=CENJBfGhoq0TSM%3A&vet=10ahUKEwiG9_z4iZThAhUFb60KHS0IDPMQMwh0KAowCg..i&w=491&h=301&bih=978&biw=1920&q=microservices&ved=0ahUKEwiG9_z4iZThAhUFb60KHS0IDPMQMwh0KAowCg&iact=mrc&uact=8

#### License

MIT