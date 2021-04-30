import requests

def get_data():
    
    x = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY')

    print(x.text)
    
    # TODO: process incoming data from JSON to dictionary or BSON
    foods_data = x.text;
    return foods_data
