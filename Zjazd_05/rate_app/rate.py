import httpx
import json

response = httpx.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/last")
print(type(response.text))
response_as_dict = json.loads(response.text)
print(type(response_as_dict))