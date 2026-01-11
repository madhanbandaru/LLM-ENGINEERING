import requests
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
def get_allLinks(url):
    try:
        web_url=requests.get(url=url,headers=headers)
        soup=BeautifulSoup(web_url.content,'html.parser')
        links=[link.get('href') for link in soup.find_all('a')]
        return list(set(links))
    except Exception as e:
        print(e)
def get_web_content(url):
    web_url=requests.get(url,headers=headers)
    soup=BeautifulSoup(web_url.content,'html.parser')
    title=soup.title.string if soup.title else "web page not found" 
    if soup.body:
        for unwanted in soup.body.find_all(['input','script','style']):
            unwanted.decompose()
        text=soup.body.get_text(separator='\n',strip=True)
    else:
        text=''
    return (title+'\n\n'+text)[:2000]