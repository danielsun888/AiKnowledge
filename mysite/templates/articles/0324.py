import requests

url="google.com"
r = requests.get(url)

print(r.status_code)