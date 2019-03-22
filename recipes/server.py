from flask import Flask, jsonify

app = Flask(__name__)

recipes = [
    {
        'name': 'pizza',
        'ingredients': ['dough', 'tomato sauce', 'cheese'],
        'instructions': [
            'Form dough',
            'Add tomato sauce',
            'Add cheese',
            'Bake in oven for 30 minutes'
        ],
    },
    {
        'name': 'pasta',
        'ingredients': ['pasta', 'tomato sauce', 'cheese'],
        'instructions': [
            'Boil pasta',
            'Add tomato sauce',
            'Add cheese',
            'Cook for 15 mins'
        ],
    },
    {
        'name': 'grilled cheese',
        'ingredients': ['bread', 'cheese', 'butter'],
        'instructions': [
            'Put bread in pan with butter',
            'Put cheese inside bread',
            'Heat on pan for 5 minutes'
        ],
    },
    {
        'name': 'garlic bread',
        'ingredients': ['bread', 'cheese', 'garlic', 'butter'],
        'instructions': [
            'Put bread in baking sheet with butter cheese and garlic',
            'Bake in oven for 15 minutes',
        ],
    },
]

@app.route('/',  methods=['GET'])
def root():
    return 'Recipes API is running.'

@app.route('/api/recipes/getAll',  methods=['GET'])
def get_recipes():
    return jsonify(recipes)