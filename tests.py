import requests

r = requests.get("https://www.daum.net")
print(r.status_code)
print(r.ok)
