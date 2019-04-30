import requests,re,json 

#Archive list#
url="https://kulturminnebilder.ra.no/fotoweb/archives/"
collectionlistH = {
    'Accept': "application/vnd.fotoware.collectionlist+json",
    'cache-control': "no-cache",
    }

rcollectionlist =  requests.request("GET", url, headers=collectionlistH)


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
  archive_url=('https://kulturminnebilder.ra.no'+(archive['href']))    

  #import requests



  headers_AL = {
    'Accept': "application/vnd.fotoware.assetlist+json",
   'cache-control': "no-cache",
    }

  AL_response = requests.request("GET", archive_url, headers=headers_AL)
  AL_Json=json.loads(AL_response.content)
  
  if not (AL_Json['paging']):
    continue
  urlpage=('https://kulturminnebilder.ra.no'+((AL_Json['paging']['next'])))
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
   urlpage=('https://kulturminnebilder.ra.no'+((next_aljson['paging']['next'])))
   
   
   

