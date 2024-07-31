fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "sweet cherries": 100,
    "pear" : 100
}

string = input("Item: ").lower()

for fruit, cal in fruits.items():
    if string.lower() == fruit:
        print(f"Calories: {cal}")
        break