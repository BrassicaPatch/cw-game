import json
from models import *

def load_cities():
    with open('city_data.json', 'r') as file:
        data = json.load(file)

    #cities = [City(item['name'], item['position']) for item in data]

    cities = [City(item['name'], item['position'], item['population'], item['income'], item['side']) for item in data]

    return cities