# WebApp-Search-Engine
search Anything on Search Engine it will collect the all the links and display in web server.

## How to Run WebApp
```
Step 1: git clone https://github.com/sujitmandal/WebApp-Search-Engine.git

Step 2: cd WebApp-Search-Engine

Step 3: pip install -r requirements.txt or pip3 install -r requirements.txt

Step 4: python app.py 

Step 5: Open browser and type http://127.0.0.1:5000/
```

## Package Installation : 
```
pip install scrape-search-engine
```
[Package Link](https://pypi.org/project/scrape-search-engine/)

## How to import the module:
```
userAgent = ('') #search on google "my user agent"
search = ('')  #Enter Anything for Search
```

## Google Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Google

googleText, googleLink = Google(search, userAgent)

print(googleText)
print(googleLink)
```
## Duckduckgo Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Duckduckgo

duckduckgoText, duckduckgoLink = Duckduckgo(search, userAgent)

print(duckduckgoText)
print(duckduckgoLink)
```
## Givewater Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Givewater

givewaterText, givewaterLink = Givewater(search, userAgent)

print(givewaterText)
print(givewaterLink)
```
## Ecosia Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Ecosia

ecosiaText, ecosiaLink = Ecosia(search, userAgent)

print(ecosiaText)
print(ecosiaLink)
```
## Bing Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Bing

bingText, bingLink = Bing(search, userAgent)

print(bingText)
print(bingLink)
```
## Yahoo Search Engine : 
```
from ScrapeSearchEngine.SearchEngine import Yahoo

yahooText, yahooLink = Yahoo(search, userAgent)

print(yahooText)
print(yahooLink)
```
## Requirement’s:
```
• Python 

• Anaconda

• Visual Studio Code
```
## LINK’S:
• [Python Download](https://www.python.org/downloads/)

• [Anaconda Download](https://www.anaconda.com/downloads)

• [Visual Studio Download](https://code.visualstudio.com/Download)

## Linux:
 How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=Mfbrxy8gK6A)](https://www.youtube.com/watch?v=Mfbrxy8gK6A "How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |")

##  Windows:
How to install | Python | | Anaconda | | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=eVV3byQlYvA)](https://www.youtube.com/watch?v=eVV3byQlYvA "How to install | Python | | Anaconda | | Opencv library |")

## Installing the required package’s:
```
• pip install scrape-search-engine

• pip install requests

• pip install flask

• pip install bs4
```
## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)