import json
from models import *

def load_cities():
    with open('cities.json', 'r') as file:
        data = json.load(file)

    cities = [City(item['name'], item['position']) for item in data]

    return cities