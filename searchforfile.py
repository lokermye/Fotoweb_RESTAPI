import requests

url = "https://kulturminnebilder.ra.no/fotoweb/archives/5003-Stavkirker/"

querystring = {"fn":"%27Hedalen_stavkirke_036.JPG%27"}


headers = {
    'Accept': "application/vnd.fotoware.assetlist+json",
    'cache-control': "no-cache"
     }

response = requests.request("GET", url,headers=headers, params=querystring)

print(response.text)