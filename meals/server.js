const express = require('express');
const graphqlHTTP = require('express-graphql');
const { buildSchema } = require('graphql');
const axios = require('axios');

const PORT = 8002;

const serviceUrlMap = {
  recipes: 'http://localhost:8000/',
  fridge: 'http://localhost:8001/',
};

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    serviceStatus(service: String!): String
  }
`);

// The root provides a resolver function for each API endpoint
const root = {
  serviceStatus: (args) => {
    const { service } = args;
    if (serviceUrlMap[service]) {
      return axios.get(serviceUrlMap[service]).then(response => response.data);
    }
    return `Service '${service}' does not exist.`;
  },
};

const app = express();

app.use('/graphql', graphqlHTTP({
  schema,
  rootValue: root,
  graphiql: true,
}));

app.listen(PORT);

console.log(`Running a GraphQL API server at localhost:${PORT}/graphql`);
