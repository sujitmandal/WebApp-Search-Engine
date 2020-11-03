from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from collections import Counter
from flask import render_template
from ScrapeSearchEngine.SearchEngine import Google
from ScrapeSearchEngine.SearchEngine import Givewater
from ScrapeSearchEngine.SearchEngine import Yahoo
from ScrapeSearchEngine.SearchEngine import Duckduckgo
from ScrapeSearchEngine.SearchEngine import Ecosia
from ScrapeSearchEngine.SearchEngine import Bing

# Github: https://github.com/sujitmandal
# This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

userAgent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


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
        duckduckgo_text = duckduckgo_text[1:11]
        duckduckgo_link = duckduckgo_link[1:11]
        duckduckgoSearch = zip(duckduckgo_link, duckduckgo_text)
        ecosia_text, ecosia_link = Ecosia(search, userAgent)
        ecosiaSearch = zip(ecosia_link, ecosia_text)
        bing_text, bing_link = Bing(search, userAgent)
        bingSearch = zip(bing_link, bing_text)

        link = []
        for i in google_link:
            link.append(i)
        for j in givewater_link:
            link.append(j)
        for k in duckduckgo_link:
            link.append(k)
        for l in yahoo_link:
            link.append(l)
        for m in ecosia_link:
            link.append(m)
        for n in bing_link:
            link.append(n)

        text = []
        for i in google_text:
            text.append(i)
        for j in givewater_text:
            text.append(j)
        for k in duckduckgo_text:
            text.append(k)
        for l in yahoo_text:
            text.append(l)
        for m in ecosia_text:
            text.append(m)
        for n in bing_text:
            text.append(n)

        commonLink = Counter(link)
        commonLinks = dict(commonLink)

        commonText = Counter(text)
        commonTexts = dict(commonText)

        finalText = []
        finalLink = []

        for text in commonTexts.items():
            finalText.append(text)

        for link in commonLinks.keys():
            finalLink.append(link)

        finalResults = zip(finalLink, finalText)

        return (render_template('result.html', googleSearch=googleSearch, givewaterSearch=givewaterSearch,
                                yahooSearch=yahooSearch, duckduckgoSearch=duckduckgoSearch, ecosiaSearch=ecosiaSearch,
                                bingSearch=bingSearch, finalResults=finalResults))
    return None


if __name__ == "__main__":
    app.run(
        port=5000
    )
