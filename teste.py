import requests

url = 'https://localhost:3000'
myobj = {'somekey': 'somevalue'}

x = requests.post(url)

print(x.text)