#print(json.dumps(data, indent=2))
# importing the requests library 
import requests 
#import re for regex
import re
#importing the pymongo library
#import pymongo
#impoerting the os library
#import os
#Accept: application/vnd.fotoware.assetlist+json
import json
#delete
url = "https://kulturminnebilder.ra.no/fotoweb/archives/5012-Byer/"

headers = {
    'Accept': "application/vnd.fotoware.assetlist+json",
    'cache-control': "no-cache",
    'Postman-Token': "11cbd20d-efcf-4093-b61c-5320529df5a8"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)
#delete

print('test of requests module')
#Archive list#
url="https://kulturminnebilder.ra.no/fotoweb/archives/"
headers = {
    'Accept': "application/vnd.fotoware.collectionlist+json",
    'cache-control': "no-cache",
    'Postman-Token': "ca8bd137-997c-4994-ba95-de936b3ccc91"
    }
r =  requests.request("GET", url, headers=headers)
#Archive list#

#archive

'/fotoweb/archives/5000-Wirefeed/?q=Tower&101=London'






#Load json#
data = json.loads(r.content)

#print some returned data 
print('Avalable Archives:')
print(len(data['data']))

#F0r Each json object#
for archive in data['data']:
  #  name= archive['data']['name']
  print(archive['name'])
  print(archive['href']) 
######DO Some Shit WHit The Data####

  #api reqest archive list#
  archive_url=('https://kulturminnebilder.ra.no'+(archive['href']))    
  print(archive_url)
  #import requests



  headers_AL = {
    'Accept': "application/vnd.fotoware.assetlist+json",
   'cache-control': "no-cache",
    'Postman-Token': "11cbd20d-efcf-4093-b61c-5320529df5a8"
   }

  AL_response = requests.request("GET", archive_url, headers=headers_AL)
  AL_Json=json.loads(AL_response.content)
  #print((AL_Json['paging']['next']))
  urlpage=('https://kulturminnebilder.ra.no'+((AL_Json['paging']['next'])))
  #OWERWRTIE IN WHILE LOOP
  #print(urlpage)
  
  print((AL_Json['paging']['last']))
  lastpage=(AL_Json['paging']['last'])
  #go thorug all pages merge json to do a doc count :) 
  doc_count=0
  page=" "
  while page  !=lastpage:
   
   next_al= requests.request("GET", urlpage, headers=headers_AL )
   next_aljson=json.loads(next_al.content)
   #print(next_al.response)
   page=(next_aljson['paging']['next'])
   numberfromstring = ((re.findall('p=\d{1,3}',page))[0])
   print( numberfromstring)
   numberfromstring =int(numberfromstring.replace('p=',''))
   print(numberfromstring)
   
   print('number of pages:')
   print((numberfromstring+1))
   print('tot number of assets:')
   #print((numberfromstring*25))
   total=(numberfromstring+1)*25
   print(total)
   page=(next_aljson['paging']['last'])
   urlpage=('https://kulturminnebilder.ra.no'+((next_aljson['paging']['next'])))
   
   
   




  #print reqest status

  #print('request status code:')
  #print(r.status_code)
  #print encoding
 #print('encoding:')
 #print(r.encoding)
 #content-type
 #print('content type:')
 #print(r.headers['content-type'])
 #print(parsed_json)
 #print(json.dumps(data, indent=2))
 #/fotoweb/archives/5000-Wirefeed/?q=fn='filnavn'

#list[-(i+1)]
