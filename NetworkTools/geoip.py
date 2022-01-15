import requests 
import json 


ip_address = input("Enter a vaild IPV4 address: ")


request_url = 'https://geolocation-db.com/jsonp/' + ip_address


response = requests.get(request_url)
result = response.content.decode()
print(result)