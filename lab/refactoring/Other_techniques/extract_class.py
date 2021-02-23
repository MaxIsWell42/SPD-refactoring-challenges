# by Kami Bigdely
# Extract Class
from pprint import pprint

class Food:
    # name = name 
    # preptime = 0
    # vege = False
    # foodtype = foodtype
    # origin = origin
    # ingredients = []
    # instructions = instructions
    
    def __init__(self, name, info):
        self.name = name
        self.preptime = info[0]
        self.vege = info[1]
        self.foodtype = info[2]
        self.origin = info[3]
        self.ingredients = info[4]
        self.instructions = info[5]
        

foods = {'butternut squash soup':[45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
          'they get soft and golden on top 2. Put all in blender with'
          'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
               '. Add coconut milk. Simmer for 5 mintues.'],
        'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                '4. Mixed them thoroughly'],
        'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

# for key, value in foods.items():
#     print("Name:",key)
#     print("Prep time:",value[0], "mins")
#     print("Is Veggie?", 'Yes' if value[1] else "No")
#     print("Food Type:", value[2])
#     print("Cuisine:", value[3])
#     for item in value[4]:
#         print(item, end=', ')
#     print()
#     print("recipe", value[5])
#     print("***")

def setRecipes(foods):
    recipeBook = []
    for k, v in foods:
        entry = Food(k, v)
        recipeBook.append(entry)
    return recipeBook


def printAll(food):
    pprint(vars(food))

