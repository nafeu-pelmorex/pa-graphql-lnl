const express = require('express');
const http = require('http');
const bodyParser = require('body-parser');

const app = express();
const server = http.Server(app);

const inventory = [
  'dough',
  'tomato sauce',
  'pepperoni',
  'tomato',
  'cheese',
  'bread',
  'garlic',
  'butter',
  'pasta',
  'bacon',
  'eggs',
  'chicken',
  'potatoes',
  'lemon juice',
  'peppers',
  'onions',
  'beef',
  'gravy',
  'lettuce',
  'mayonaise',
  'dressing',
  'olives',
];

server.listen(process.env.PORT || 8001, () => {
  console.log(`[ server.js ] Listening on port ${server.address().port}`);
});

app.use(bodyParser.urlencoded({
  extended: true,
}));

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.status(200).send('Fridge API is running.');
});

app.get('/api/inventory/getAll', (req, res) => {
  res.json(inventory);
});
