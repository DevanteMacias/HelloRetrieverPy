from urllib import response
import requests
import json
from pprint import pprint
import creds

# header for api call
hed = {'Authorization': 'Bearer ' + creds.api_key}

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
