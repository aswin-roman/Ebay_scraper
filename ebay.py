from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://www.ebay-kleinanzeigen.de/s-chemnitz/bettgestell/k0l3869'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)
content = response.content

soup = BeautifulSoup(content,features="html.parser")
heads = []
data = []
links = []

for ad in soup.findAll(name='article',attrs={'class':'aditem'}):
    main = ad.find('a',href=True,attrs={'class':'ellipsis'})
    heads.append(main.text)
    info = "".join(ad.find('div', attrs={'class': 'aditem-details'}).text).split()
    data.append(info)
    link = 'https://www.ebay-kleinanzeigen.de' + main.get('href')
    links.append(link)

df = pandas.DataFrame({"Head":heads,"Data":data,"Link":links})
df.to_csv('bettgestell.csv', index=False, encoding='utf-8')
