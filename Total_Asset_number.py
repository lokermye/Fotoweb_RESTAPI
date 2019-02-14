import requests,re,json 

baseurl="https://kulturminnebilder.ra.no"

#api descritor headder#
apidescripH={
    'Accept': "application/vnd.fotoware.api-descriptor+json",
    'cache-control': "no-cache",
    }
              
#colection list headder#

collectionlistH = {
    'Accept': "application/vnd.fotoware.collectionlist+json",
    'cache-control': "no-cache",
    }
#asset list headder
headers_AL = {
    'Accept': "application/vnd.fotoware.assetlist+json",
    'cache-control': "no-cache",
    }

rapidescritor= requests.request("GET", baseurl, headers=apidescripH)
rapidescrptorjson= json.loads(rapidescritor.content)
archives_url=baseurl+(rapidescrptorjson["archives"])





rcollectionlist =  requests.request("GET", archives_url, headers=collectionlistH)


#Load json#
data = json.loads(rcollectionlist.content)

#print some returned data 
print('Avalable Archives:')
print(len(data['data']))

#F0r Each json object#
for archive in data['data']:
  #  name= archive['data']['name']
  print(archive['name'])
  #api reqest archive list#
  archive_url=(baseurl+(archive['href']))    

  #import requests



  

  AL_response = requests.request("GET", archive_url, headers=headers_AL)
  AL_Json=json.loads(AL_response.content)

  urlpage=(baseurl+((AL_Json['paging']['next'])))
  #OWERWRTIE IN WHILE LOOP


  lastpage=(AL_Json['paging']['last'])
  #go thorug all pages merge json to do a doc count :) 
  doc_count=0
  page=" "
  while page  !=lastpage:
   
   next_al= requests.request("GET", urlpage, headers=headers_AL )
   next_aljson=json.loads(next_al.content)

   page=(next_aljson['paging']['next'])
   numberfromstring = ((re.findall('p=\d{1,3}',page))[0])

   numberfromstring =int(numberfromstring.replace('p=',''))
   print('number of pages:')
   print((numberfromstring+1))
   print('tot number of assets:')
   total=(numberfromstring+1)*25
   print(total)
   page=(next_aljson['paging']['last'])
   urlpage=(baseurl+((next_aljson['paging']['next'])))
   
   
   
