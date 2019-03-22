const express = require('express');
const graphqlHTTP = require('express-graphql');
const { buildSchema } = require('graphql');
const axios = require('axios');
const _ = require('lodash');

const PORT = 8002;

const serviceUrlMap = {
  recipes: 'http://localhost:8000/',
  fridge: 'http://localhost:8001/',
};

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    serviceStatus(service: String!): String
    inventory: [String]
    inventoryHas(ingredient: String!): Boolean
    Recipe(name: String): Recipe
    allRecipes: [Recipe]
    availableRecipes: [Recipe]
  }

  type Recipe {
    name: String
    ingredients: [String]
    instructions: [String]
  }
`);

class Recipe {
  constructor({ name, ingredients, instructions }) {
    this.name = name;
    this.ingredients = ingredients;
    this.instructions = instructions;
  }
}

// The root provides a resolver function for each API endpoint
const root = {
  serviceStatus: (args) => {
    const { service } = args;
    if (serviceUrlMap[service.toLowerCase()]) {
      return axios.get(serviceUrlMap[service.toLowerCase()]).then(response => response.data);
    }
    return `Service '${service}' does not exist.`;
  },
  inventory: () => axios.get(`${serviceUrlMap.fridge}api/inventory/getAll`)
    .then(response => response.data),
  inventoryHas: args => axios.get(`${serviceUrlMap.fridge}api/inventory/getAll`)
    .then((response) => {
      const { ingredient } = args;
      if (_.includes(response.data, ingredient.toLowerCase())) {
        return true;
      }
      return false;
    }),
  Recipe: args => axios.get(`${serviceUrlMap.recipes}api/recipes/getAll`)
    .then((response) => {
      const recipe = _.find(response.data, { name: args.name.toLowerCase() });
      if (recipe) {
        return new Recipe(recipe);
      }
      return null;
    }),
  allRecipes: () => axios.get(`${serviceUrlMap.recipes}api/recipes/getAll`)
    .then((response) => {
      const recipes = [];
      _.each(response.data, (recipe) => {
        recipes.push(new Recipe(recipe));
      });
      return recipes;
    }),
  availableRecipes: async () => {
    const availableRecipes = [];
    const { data: inventory } = await axios.get(`${serviceUrlMap.fridge}api/inventory/getAll`);
    const { data: recipes } = await axios.get(`${serviceUrlMap.recipes}api/recipes/getAll`);
    _.each(recipes, (recipe) => {
      if (_.difference(recipe.ingredients, inventory).length < 1) {
        availableRecipes.push(new Recipe(recipe));
      }
    });
    return availableRecipes;
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
