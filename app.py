from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
from ScrapeSearchEngine.SearchEngine import Google
from ScrapeSearchEngine.SearchEngine import Givewater
from ScrapeSearchEngine.SearchEngine import Yahoo 
from ScrapeSearchEngine.SearchEngine import Duckduckgo
from ScrapeSearchEngine.SearchEngine import Ecosia
from ScrapeSearchEngine.SearchEngine import Bing

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

userAgent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return(render_template('home.html'))

def Dictionary(keys, values):
    key = []
    value = []

    for i in keys:
        key.append(i)

    for j in values:
        value.append(j)

    commonDictionary = dict(zip(key, value))
    return(commonDictionary)

@app.route('/result', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		search = request.form['txt_search']
		google_text, google_link = Google(search, userAgent)
		googleSearch = zip(google_link, google_text)
		givewater_text, givewater_link = Givewater(search, userAgent)
		givewaterSearch = zip(givewater_link, givewater_text)
		yahoo_text, yahoo_link = Yahoo(search, userAgent)
		yahooSearch = zip(yahoo_link, yahoo_text)
		duckduckgo_text, duckduckgo_link = Duckduckgo(search, userAgent)
		duckduckgoSearch = zip(duckduckgo_link, duckduckgo_text)
		ecosia_text, ecosia_link = Ecosia(search, userAgent)
		ecosiaSearch = zip(ecosia_link, ecosia_text)
		bing_text, bing_link = Bing(search, userAgent)
		bingSearch = zip(bing_link, bing_text)

		googleSet = set(google_link)
		givewaterSet = set(givewater_link)
		duckduckgoSet = set(duckduckgo_link)
		ecosiaSet = set(ecosia_link)
		bingSet = set(bing_link)
		yahooSet = set(yahoo_link)

		intersection1 = googleSet.intersection(givewaterSet)
		intersection2 = intersection1.intersection(ecosiaSet)
		intersection3 = intersection2.intersection(bingSet)
		intersection4 = intersection3.intersection(duckduckgoSet)
		intersection5 = intersection4.intersection(yahooSet)
		
		intersectionList = list(intersection5)
		
		finalLink = []
		for i in intersectionList:
			finalLink.append(i)

		dictionary = Dictionary(google_text, google_link)
		finalKey = []

		for j in finalLink:
			for key , value in dictionary.items():
				if j == value:
					finalKey.append(key)

		commonLink = zip(finalLink, finalKey)
		return(render_template('result.html', googleSearch=googleSearch, givewaterSearch=givewaterSearch, yahooSearch=yahooSearch, duckduckgoSearch=duckduckgoSearch, ecosiaSearch=ecosiaSearch, bingSearch=bingSearch, commonLink=commonLink))
	return(None)

if __name__ == "__main__":
	app.run(
		port=5000
		)
