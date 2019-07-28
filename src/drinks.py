# drinks.py

drink_list = [
    {
        "name": "Gin Tonic",
        "recipe": [
            ("tonic", 135),
            ("gin", 45)
        ]
    }, {
        "name": "Virgin Sunrise",
        "img": "vs.png",
        "recipe": [
            ("oj", 160),
            ("gren", 8)
        ]
    }, {
        "name": "Cuba Libre",
        "recipe": [
            ("cola", 135),
            ("bacardi", 45),
            ("limejuice", 5)
        ]
    }, {
        "name": "PineMate",
        "recipe": [
            ("mate", 100),
            ("pineapple", 75),
            ("curacao", 16)
            #("cocos", 20)
        ]
    }, {
        "name": "Tschunk",
        "recipe": [
            ("bacardi", 20),
            ("mate", 120)
        ]
    }, {
        "name": "Exotic",
        "recipe": [
            ("oj", 90),
            ("pineapple", 60),
            ("mango", 30),
            ("curacao", 16)
            #("cocos", 16)
        ]
    }, {
        "name": "Vodka-O",
        "recipe": [
            ("vodka", 45),
            ("oj", 135)
        ]
    }, {
        "name": "...under\nconstruction",
        "recipe": [
        ]
    }, {
        "name": "...under\nconstruction",
        "recipe": [
        ]
    }, {
        "name": "...under\nconstruction",
        "recipe": [
        ]
    }, {
        "name": "Bo",
        "recipe": [
            ("oj", 120),
            ("bacardi", 40)
        ]
    }, {
        "name": "Bs",
        "recipe": [
            ("oj", 120),
            ("bacardi", 40),
            ("gren", 8)
        ]
    }, {
        "name": "Happy",
        "recipe": [
            ("mate", 100),
            ("mango", 50),
            ("lemonjuice", 20)
        ]
    }, {
        "name": "Ts 1",
        "recipe": [
            ("bacardi", 40),
            ("mate", 300)
        ]
    }, {
        "name": "...under\nconstruction",
        "recipe": [
        ]
    }

]

# "NAME":("NICENAME", ISWITHALCOHOL)
ingredients = {
    "gren": ("Grenadine", False),
    "cocos": ("Cocos", False),
    "lemonjuice": ("Lemon Juice", False),
    "limejuice": ("Lime Juice", False),
    "bacardi": ("Bacardi", True),
    "rum": ("Rum", True),
    "vodka": ("Vodka", True),
    "gin": ("Gin", True),
    "curacao": ("Blue Curacao", False),
    "mango": ("Mango", False),
    "pineapple": ("Pineapple", False),
    "tequila": ("tequila", False),
    "cola": ("Cola", False),
    "oj": ("Orange Juice", False),
    "mate": ("Mate", False),
    "tonic": ("Tonic Water", False)
}


