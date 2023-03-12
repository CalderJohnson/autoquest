"""Code pertaining to determining their vehicle based on the form"""
from pydantic import BaseModel
from copy import deepcopy

#hardcoded database of ford models
data = [
    {
        "name": "F-150",
        "type": "truck",
        "price": 34445,
        "engine": "hybrid",
        "seats": 6,
        "uses": ["camping", "towing", "worktable", "loading", "offroad", "performance"],
        "allterrain": True,
    },

    {
        "name": "F-150",
        "type": "truck",
        "price": 34445,
        "engine": "gas",
        "seats": 6,
        "uses": ["camping", "towing", "worktable", "loading", "offroad"],
        "allterrain": True,
    },

    {
        "name": "Mustang",
        "type": "sports",
        "price": 27770,
        "engine": "gas",
        "seats": 4,
        "uses": ["performance", "track", "fashion"],
        "allterrain": False, 
    },

    {
        "name": "Bronco",
        "type": "suv",
        "price": 34095,
        "engine": "gas",
        "seats": 4,
        "uses": ["camping", "offroad", "fashion"],
        "allterrain": True 
    },

    {
        "name": "Bronco Sport",
        "type": "suv",
        "price": 29215,
        "engine": "gas",
        "seats": 4,
        "uses": ["camping", "offroad", "performance"],
        "allterrain": True 
    },

    {
        "name": "Ford GT",
        "type": "sports",
        "price": 1700000,
        "engine": "gas",
        "seats": 2,
        "uses": ["track", "performance", "speed", "hypercar"],
        "allterrain": False 
    },

    {
        "name": "EcoSport",
        "type": "suv",
        "price": 22040,
        "engine": "gas",
        "seats": 5,
        "uses": ["everyday", "family", "safety", "economic", "performance"],
        "allterrain": False 
    },

    {
        "name": "Escape",
        "type": "suv",
        "price": 28000,
        "engine": "hybrid",
        "seats": 5,
        "uses": ["safety", "family", "everyday", "economic", "comfort"],
        "allterrain": False 
    },

    {
        "name": "Edge",
        "type": "suv",
        "price": 37945,
        "engine": "gas",
        "seats": 5,
        "uses": ["safety", "family", "everyday", "economic", "comfort"],
        "allterrain": False 
    },

    {
        "name": "Mustang Mach-e",
        "type": "suv",
        "price": 45995,
        "engine": "electric",
        "seats": 5,
        "uses": ["safety", "family", "everyday", "economic", "fashion", "performance"],
        "allterrain": False 
    },

    {
        "name": "Expedition",
        "type": "suv",
        "price": 55125,
        "engine": "electric",
        "seats": 8,
        "uses": ["camping", "family", "everyday", "economic"],
        "allterrain": True 
    },

    {
        "name": "Maverick",
        "type": "truck",
        "price": 22595,
        "engine": "hybrid",
        "seats": 5,
        "uses": ["camping", "towing", "worktable", "loading", "offroad"],
        "allterrain": True,
    },

    {
        "name": "Ranger",
        "type": "truck",
        "price": 27400,
        "engine": "gas",
        "seats": 5,
        "uses": ["camping", "towing", "worktable", "loading", "offroad"],
        "allterrain": True,
    },

    {
        "name": "Super-Duty",
        "type": "truck",
        "price": 43970,
        "engine": "gas",
        "seats": 6,
        "uses": ["camping", "towing", "worktable", "loading", "offroad"],
        "allterrain": True,
    },

    {
        "name": "Lightning",
        "type": "truck",
        "price": 55974,
        "engine": "electric",
        "seats": 5,
        "uses": ["camping", "towing", "worktable", "loading", "offroad"],
        "allterrain": True,
    },
]

class CarForm(BaseModel):
    """Form data model"""
    type: str | None = None
    engine: str | None = None
    price: int
    seats: int | None = None
    uses: list = []
    allterrain: bool

def calculate_car(form: CarForm):
    """Determine optimal car based on form data"""
    filterable = deepcopy(data)

    #filter those with incompatible pricing
    for car in filterable:
        if car["price"] > form.price:
            filterable.remove(car)

    #return car with most category matches
    for car in filterable:
        car["score"] = 0

        #distinct categories worth 5 points
        if car["type"] == form.type:
            car["score"] += 5
        if car["engine"] == form.engine:
            car["score"] += 5
        if car["allterrain"] == form.allterrain:
            car["score"] += 5

        #seat points worth 3 - difference of what is desired
        if form.seats is not None:
            car["score"] += 3 - abs(car["seats"] - form.seats)
        
        #uses worth 1 each
        if form.uses is not None:
            for use in car["uses"]:
                if use in form.uses:
                    car["score"] += 1

    #return car with highest score
    return sorted(filterable, key=lambda x: x["score"], reverse=True)[0]
