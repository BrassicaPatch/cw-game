from openai import OpenAI
from pathlib import Path
import os
import json
import city

def get_income(message):

    path = Path('income_output.json')
    if path.exists():
        with path.open('r') as file:
            data = json.load(file)
            city_incomes = [(city, income) for city, income in data.items()]
            return city_incomes

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are helping to develop a simple Civil War Strategy Game"},
        {"role": "user", "content": message}
    ]
    )

    print(completion.choices[0].message)

    income_json = completion.choices[0].message.content
    income_json_cleaned = income_json.replace('\n', '').replace('json', '').replace('`', '')

    if not income_json_cleaned.strip():
        print("The JSON string is empty")
    else:
        try:
            decoded_json = json.loads(income_json_cleaned)
        except json.JSONDecodeError as e:
            print(f'Invalid JSON: {e}')

    city_incomes = [(city, income) for city, income in decoded_json.items()]

    with open('income_output.json', 'w') as json_file:
        json.dump(decoded_json, json_file, indent=4)

    return city_incomes


def get_pop(message):

    path = Path('pop_output.json')
    if path.exists():
        with path.open('r') as file:
            data = json.load(file)
            city_pops = [(list(item.keys())[0], list(item.values())[0]) for item in data]
            return city_pops

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are helping to develop a simple Civil War Strategy Game"},
        {"role": "user", "content": message}
    ]
    )

    print(completion.choices[0].message)

    pop_json = completion.choices[0].message.content
    pop_json_cleaned = pop_json.replace('\n', '').replace('json', '').replace('`', '')

    if not pop_json_cleaned.strip():
        print("The JSON string is empty")
    else:
        try:
            decoded_json = json.loads(pop_json_cleaned)
        except json.JSONDecodeError as e:
            print(f'Invalid JSON: {e}')

    city_pops = [(list(item.keys())[0], list(item.values())[0]) for item in decoded_json]

    with open('pop_output.json', 'w') as json_file:
        json.dump(decoded_json, json_file, indent=4)

    return city_pops

def get_connections(city_names):

    path = Path('cons_output.json')
    if path.exists():
        with path.open('r') as file:
            data = json.load(file)
            city_cons = [(list(item.keys())[0], list(item.values())[0]) for item in data]
            return city_cons

    count = 1
    city_connections = []
    for city in city_names:
    
        formatting = "{ \"Washington DC\": [ {\"city\": \"Baltimore\", \"railroad\": true}, { \"city\": \"Frederick\", \"railroad\": true} ]}"
        message = f"An initial single city will be provided. Give its immediate neighbor connections to cities listed in the following total city list, and specifiy if the connection is a railroad. Return this in JSON formatting, and dont give any other description. Please use this fomratting: {formatting}. City: {city} Cities: {city_names}"

        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are helping to develop a simple Civil War Strategy Game"},
            {"role": "user", "content": message}
        ]
        )


        income_json = completion.choices[0].message.content
        income_json_cleaned = income_json.replace('\n', '').replace('json', '').replace('`', '')

        if not income_json_cleaned.strip():
            print("The JSON string is empty")
        else:
            try:
                decoded_json = json.loads(income_json_cleaned)
            except json.JSONDecodeError as e:
                print(f'Invalid JSON: {e}')

        for main_city, neighbors in decoded_json.items():
            connections = [(neighbor["city"], neighbor["railroad"]) for neighbor in neighbors]
            city_connections.append((main_city, connections))

        print(f'Completed Connections {count} / {len(city_names)}')
        count += 1

    with open('cons_output.json', 'w') as json_file:
        json.dump(city_connections, json_file, indent=4)

    return city_connections

with open('city_data.json', 'r') as file:
    data = json.load(file)

cities = [city.City(item['name'], item['position'], item['population'], item['income'], item['side']) for item in data]

city_names = [item.name for item in cities]



income_message = f"For each of the provided cities, give an abstract income value, with 200 being the max, relative to the 1860s Pre-Civil War economy. A list of cities and their populations will also be provided. They should be relatively similar in scale relative to other cities. Return a JSON of the city name and the integar income value it has. Do not give any other description. Cities: {city_names}"
city_incomes = get_income(income_message)[:20]

pop_message = f"For each of the provided cities, give a abstract population value, relative to the 1860s Pre-Civil War US. Return a JSON of the city name and the integar population value it has. Do not give any other description. Cities and Incomes: {city_incomes}"
city_pops = get_pop(pop_message)

city_cons = get_connections(city_names)