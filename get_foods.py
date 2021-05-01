import requests
# from flask import jsonify

def get_data():
    
    x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Bread')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY')
    # x = requests.get('https://api.nal.usda.gov/fdc/v1/json-spec?api_key=DEMO_KEY')

    foods_list = x.json()

    print(foods_list)
    
    return foods_list
