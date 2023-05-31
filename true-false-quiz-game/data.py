import requests
import pprint

# Parameters using
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,     # Science: Computers
}

# Unescaping HTML entities>
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]