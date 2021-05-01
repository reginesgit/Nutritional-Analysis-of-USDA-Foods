import requests
from flask import jsonify

def get_data():
    
    x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=EgSU9SSdsXlWhwfDCPLn1DwOsZBLZGQVjNXRRooS&query=Cheese')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=EgSU9SSdsXlWhwfDCPLn1DwOsZBLZGQVjNXRRooS')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/json-spec?api_key=DEMO_KEY')

    foods_list = x.json()

    # Python3 program to Convert a list to dictionary
    # def Convert(foods_list):
    #     foods_dct = {foods_list[i]: foods_list[i + 1] for i in range(0, len(foods_list), 2)}
    #     return foods_dct
            
    # foods_data = Convert(foods_list);
    # print(foods_data)

    print(foods_list)
    
    # TODO: process incoming data from JSON to dictionary or BSON
    # foods_data = x.text;
    return foods_list
