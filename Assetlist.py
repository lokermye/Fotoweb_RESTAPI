
import requests

url = "https://kulturminnebilder.ra.no/fotoweb/archives/5012-Byer/"

headers = {
    'Accept': "application/vnd.fotoware.assetlist+json",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
