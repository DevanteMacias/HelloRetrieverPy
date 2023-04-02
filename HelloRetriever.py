import requests
from dotenv import main
import os

# load env vars, save api key value
main.load_dotenv(".env")
API_KEY = os.getenv('API_KEY')

# header for api call
hed = {'Authorization': 'Bearer ' + API_KEY}

# uri for RESTful GET
uri = 'https://app.helloretriever.com/api/v1/device_returns/'

# GET call to Hello Retreiver
r = requests.get(uri, headers=hed)

# turning GET into json
r_json = r.json()

# defining results dictionary
results = r_json['results']

for result in results:
    for shipment in result['shipments']:
        if shipment['status'] != ('return_complete'):
            print(result['id'],shipment['status'],result['purchaser_email'])
