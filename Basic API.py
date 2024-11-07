'''
from fastapi import FastAPI

app = FastAPI()

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: str):
    if cuisine not in valid_cuisines:
        return {"error": f"Supported cuisines are {list(valid_cuisines)}"}
    
    return {"items": food_items.get(cuisine)}
'''
#2. Coding the exception
'''
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str,Enum):
    indian = "indian",
    american = "american",
    italian = "italian"

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines): 
    return food_items.get(cuisine)
'''

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str,Enum):
    indian = "indian",
    american = "american",
    italian = "italian"

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines): 
    return food_items.get(cuisine)

coupon_code = {
    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code)}
