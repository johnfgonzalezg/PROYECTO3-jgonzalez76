import requests # type: ignore

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
