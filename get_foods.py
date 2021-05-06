import requests
from config import API_KEY
# from flask import jsonify

def get_data():
    
    query = "Milk"

    url = "https://api.nal.usda.gov/fdc/v1/foods/search?"

    query_url = f"{url}api_key={API_KEY}&query={query}"

    x = requests.get(query_url)
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Bread')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/json-spec?api_key=DEMO_KEY')

    foods_list = x.json()

    print(foods_list)
    
    return foods_list
