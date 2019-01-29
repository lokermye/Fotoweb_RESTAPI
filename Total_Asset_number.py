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

print('test of requests module')
#Archive list#
url="https://kulturminnebilder.ra.no/fotoweb/archives/"
headers = {
    'Accept': "application/vnd.fotoware.collectionlist+json",
    'cache-control': "no-cache",

    }
r =  requests.request("GET", url, headers=headers)
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

   }

  AL_response = requests.request("GET", archive_url, headers=headers_AL)
  AL_Json=json.loads(AL_response.content)
  #print((AL_Json['paging']['next']))
  urlpage=('https://kulturminnebilder.ra.no'+((AL_Json['paging']['next'])))
  lastpageurl=('https://kulturminnebilder.ra.no'+((AL_Json['paging']['last'])))
  #OWERWRTIE IN WHILE LOOP
  #print(urlpage)

  print((AL_Json['paging']['last']))
  lastpage=(AL_Json['paging']['last'])
  page=' '
  #use first page to
  while page  !=lastpage:
   print("--------------")
   next_al= requests.request("GET", urlpage, headers=headers_AL )
   next_aljson=json.loads(next_al.content)
   page=(next_aljson['paging']['last'])
   print urlpage
   print lastpageurl
   if urlpage != lastpageurl :
       numberfromstring = ((re.findall('p=\d{1,3}',page))[0])
       numberfromstring =int(numberfromstring.replace('p=',''))

   #page=(next_aljson['paging']['last'])
   urlpage=('https://kulturminnebilder.ra.no'+((next_aljson['paging']['last'])))


   test=(next_aljson['data'][1]['filename'])
   data=(next_aljson['data'])
   print(test)
   print(len(data) )
   print(numberfromstring)

   print('number of pages:')
   print((numberfromstring+1))
   print('tot number of assets:')
   total=(numberfromstring+1)*25
   print(total)
   #end






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
