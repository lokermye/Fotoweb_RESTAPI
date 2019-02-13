import requests

url = "https://kulturminnebilder.ra.no/"

headers = {
    'Accept': "application/vnd.fotoware.api-descriptor+json"
          }

response = requests.request("GET", url, headers=headers)

print(response.text)
