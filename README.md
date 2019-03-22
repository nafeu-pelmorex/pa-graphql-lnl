# Pelmorex Audience - GraphQL Lunch & Learn

Demo project for the GraphQL lunch & learn which took place on March 2019 at Pelmorex LV office.

### Requirements

Python 3
Node.js >= v8

### Setup & Installation

#### Recipes API

Installation:

```
cd recipes
. venv/bin/activate
pip install -r requirements.txt
```

Running the server:

```
export FLASK_APP=server.py
flask run --port=8000
```

Send requests to `localhost:8000/`

#### Fridge API

Installation

```
cd fridge
npm install
```

Running the server:

```
npm start
```

Send requests to `localhost:8001/`

#### Meals API

Installation

```
cd meals
npm install
```

Running the server:

```
npm start
```

Send queries to `localhost:8002/graphql`

### Presentation Notes

We want to demonstrate how graphql can be used to replace REST apis (with new Graph API)

RecipesAPI => Flask App (Python)
FridgeAPI => Express App (Node.js)
MealsAPI => GraphQL API Gateway (Node.js)

Questions to Answer:

- Difference between REST and GraphQL

The core difference between GraphQL and REST can be boiled down as follows:

REST has a set of endpoints that each return fixed data structures
GraphQL has a single endpoint that returns flexible data structures

- What is monolithic architecture?
- What are microservices?
- What are advantages of monolith versus microservices?

Resources:

https://www.google.ca/imgres?imgurl=https%3A%2F%2Fd1.awsstatic.com%2FDeveloper%2520Marketing%2Fcontainers%2Fmonolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png&imgrefurl=https%3A%2F%2Faws.amazon.com%2Fmicroservices%2F&docid=v5_ybMDNzBRAKM&tbnid=CENJBfGhoq0TSM%3A&vet=10ahUKEwiG9_z4iZThAhUFb60KHS0IDPMQMwh0KAowCg..i&w=491&h=301&bih=978&biw=1920&q=microservices&ved=0ahUKEwiG9_z4iZThAhUFb60KHS0IDPMQMwh0KAowCg&iact=mrc&uact=8

https://www.prisma.io/blog/how-to-wrap-a-rest-api-with-graphql-8bf3fb17547d

#### License

MIT