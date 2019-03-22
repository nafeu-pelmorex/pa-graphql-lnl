from flask import Flask, jsonify

app = Flask(__name__)

recipes = [
    {
        'name': 'cheese pizza',
        'ingredients': ['dough', 'tomato sauce', 'cheese'],
        'instructions': [
            'Form dough',
            'Add tomato sauce',
            'Add cheese',
            'Bake in oven for 20 minutes'
        ],
    },
    {
        'name': 'vegetarian pizza',
        'ingredients': ['dough', 'tomato sauce', 'cheese', 'peppers', 'onions', 'olives'],
        'instructions': [
            'Form dough',
            'Add tomato sauce',
            'Add cheese',
            'Add vegetables',
            'Bake in oven for 20 minutes'
        ],
    },
    {
        'name': 'meatlovers pizza',
        'ingredients': ['dough', 'tomato sauce', 'cheese', 'bacon', 'chicken', 'pepperoni'],
        'instructions': [
            'Form dough',
            'Add tomato sauce',
            'Add cheese',
            'Prepare and add meat',
            'Bake in oven for 20 minutes'
        ],
    },
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
    {
        'name': 'carbanara',
        'ingredients': ['eggs', 'bacon', 'pasta'],
        'instructions': [
            'Cook bacon',
            'Boil pasta',
            'Mix pasta with bacon',
            'Mix with egg'
        ]
    },
    {
        'name': 'lemon chicken',
        'ingredients': ['chicken', 'potatoes', 'lemon juice'],
        'instructions': [
            'Preheat oven',
            'Prepare chicken and potatoes',
            'Mix with lemon juice',
            'Bake'
        ]
    },
    {
        'name': 'bacon and eggs',
        'ingredients': ['bacon', 'eggs'],
        'instructions': [
            'Cook them in pan'
        ]
    },
    {
        'name': 'mac and cheese',
        'ingredients': ['butter', 'cheese', 'pasta'],
        'instructions': [
            'Boil pasta',
            'Cook in pan with cheese and butter'
        ]
    },
    {
        'name': 'poutine',
        'ingredients': ['gravy', 'potatoes', 'cheese'],
        'instructions': [
            'Cut and prepare potatoes',
            'Present heated with gravy and cheese',
        ]
    },
    {
        'name': 'blt sandwich',
        'ingredients': ['bread', 'bacon', 'lettuce', 'tomato', 'mayonaise'],
        'instructions': [
            'Slice bread',
            'Put bacon, lettuce, tomato and mayo in sandwich'
        ]
    },
    {
        'name': 'salad',
        'ingredients': ['onions', 'lemon juice', 'salad dressing', 'lettuce', 'tomato', 'peppers']
    }
]

@app.route('/',  methods=['GET'])
def root():
    return 'Recipes API is running.'

@app.route('/api/recipes/getAll',  methods=['GET'])
def get_recipes():
    return jsonify(recipes)