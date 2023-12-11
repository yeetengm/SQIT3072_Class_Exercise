# Bank Negara Malaysia API Testing


import requests
import json
from pprint import pprint           # Bagi cantik
import matplotlib.pyplot as plt

# API point is from " https://apikijangportal.bnm.gov.my "

# Define the endpoint URL (Uniform Resource Identifier)
endpoint_url = "https://api.bnm.gov.my/public/fx-turn-over"  

# Define the header parameters # USE VERSION PYTHON 3.9.18
headers = {
    "Accept": "application/vnd.BNM.API.v1+json"
}

# Make the GET request
response = requests.get(endpoint_url, headers=headers)      # 当我们send request，我们会得到response，所以 response = request （因果关系）

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Print or manipulate the data as needed
    pprint(data)
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")