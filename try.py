import requests
import urllib.parse

class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method
        
        
request=Request('GET', {'search':"Galvin"})

if request.method =='GET':
    search=urllib.parse.quote(request.args.get('search',''))
    url=f"http://openlibrary.com/books/v1/volumes?q={search}&maxResults=3"
    response=requests.get(url)
    #print(response.json())
    
    if response.status_code==200:
        data= response.json()
        for item in data.get('items',[]):
            volume_info = item.get('volumeInfo',{})
            title=volume_info.get('title','N/A')
            print(title)