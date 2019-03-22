# PA - GraphQL Lunch & Learn

Demo project for the GraphQL lunch & learn which took place on March 2019 at Pelmorex LV office.

## Requirements

Python 3
Node.js >= v8

## Setup & Installation

### Recipes API

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

### Fridge API

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

### Meals API

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

#### Demo

Use **ngrok** (`npm install -g ngrok`) like so:

```
ngrok http 8002
```

Share the public link to all of your audience members

#### License

MIT