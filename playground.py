import urllib
from bs4 import BeautifulSoup
# print (wikia.page("harrypotter", "Harry_Potter").title)
import requests

from person import UserBase
tst = []
import json

import pickle
from FuzzySearch import FuzzySearch


# print(urllib.parse.urljoin("https://harrypotter.fandom.com", "/wiki/Lovegood_House"))

# data = requests.get("https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Half-Blood_Prince").text
# soup = BeautifulSoup(data, features="html.parser")
# with open("debug2.html", "w") as f:
#     f.write(str(soup))


# title = soup.find("meta", {"property": "og:title"})

# print(title.get("content").lower())


# desc = soup.find("div", {"id": "mw-content-text"})
# desc = desc.find("div", {"class": "mw-parser-output"}, recursive=False)
# paragraphs = desc.find_all("p", {'class': None}, recursive=False)
# debug = {"db": []}
# for p in paragraphs:
#     if p.find("aside") == None:
#         debug['db'].append(p.getText())
# with open("debug.json", "w") as f:
    
#     f.write(json.dumps(debug, indent=1))
# text = ''
# for p in paragraphs:
#     text = text + p.text
# print(text)

# def run(test):
#     test.append("peepee")


# print(tst)
# run(tst)
# print(tst)

# with open('knowledge_base.pickle', 'rb') as handle:
#     knowlage_base = pickle.load(handle)


# search = FuzzySearch(knowlage_base)

# print(search.find("JK Rowling"))
userbase = UserBase()
with open("userbase.json", "w") as f:
    f.write(json.dumps(userbase.dict, indent=1))