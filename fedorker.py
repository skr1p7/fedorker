import requests
from bs4 import BeautifulSoup

def bing():
    vulnAd = []
    dork = input("Enter the dork> ")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    req = requests.get('https://www.bing.com/search?q={}'.format(str(dork)), headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all('li', class_='b_algo')
    for link in results:
        vulnAd.append(link.find('a').attrs['href'])
    return vulnAd

def google():
    vulnAd = []
    dork = input("Enter the dork> ")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    req = requests.get('http://www.google.com/search?q={}'.format(str(dork)), headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.findAll('cite',attrs={'class':'iUlink0'})
    for link in results:
        vulnAd.append(link.text)
    return vulnAs
  
browser = str(input("Enter the search engine name> "))
if browser == "google":
    print (*google(), sep="\n")
if browser == "bing":
    print (*bing(), sep="\n")
