spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    lst =  [f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']*'🌶'}" for food in spicy_foods]
    for f in lst:
        print(f)
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food["cuisine"]== cuisine][0]

def print_spiciest_foods(spicy_foods):
    lst = [f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}" for food in spicy_foods if food["heat_level"]>5]
    for f in lst:
        print(f)

def get_average_heat_level(spicy_foods):
    spicy_level = [food["heat_level"] for food in spicy_foods]
    total = 0
    for level in spicy_level:
        total += level
    return total//len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
