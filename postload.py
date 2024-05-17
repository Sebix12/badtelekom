import requests

url = 'https://data-api.downdetector.com/v1/companies/39226/rating?rating=1'
myobj = {'rating': '1'}

for x in range(6):
    x = requests.post(url, json = myobj)

print(x.text)