import urllib
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import requests
import nltk
import json
import random
import pickle


knowledge_base = {}
visited_urls = []


def main():
    starter_url = "https://harrypotter.fandom.com/wiki/Harry_Potter"

    crawl(starter_url, 20)

    with open("knowledge_base.json", "w") as f:
        f.write(json.dumps(knowledge_base, indent=1))
    with open("knowledge_base.pickle", "wb") as f:
            pickle.dump(knowledge_base, f)


def crawl(starter_url, link_limit=20):
    
    _crawl(starter_url, 4, link_limit)

    


def _crawl(starter_url, depth, link_limit): 
    print("Depth: ", depth)
    print("Visited urls", visited_urls)
    # check to see if we've been her ebefore
    if starter_url in visited_urls: 
        print("Skipping: Visited!")
        return

    
    
    
    
    parent_url_parse = urlparse(starter_url)
    domain = parent_url_parse.netloc

    

    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data, features="html.parser")

    try:
        if soup.find("html").get("lang") != 'en': # make sure we only travel to english pages
            print("Skipping: Not english!")
            return
    except:
        return
    if depth > 0: 
        with open("knowledge_base.json", "w") as f:
            f.write(json.dumps(knowledge_base, indent=1))
        with open("knowledge_base.pickle", "wb") as f:
            pickle.dump(knowledge_base, f)

    #get the summery and save it in the knowlage base
    #title = soup.find("h1", {"id": "firstHeading"})
    try: 
        title = soup.find("meta", {"property": "og:title"})
        if title == None: 
            print("Skipping: No Title!")
        else:

            title = title.get("content").lower()
            #title = title.getText().lower()
            title = re.sub('[^A-Za-z0-9 ]+', '', title)
        # Parse out the summary

        desc = soup.find("div", {"id": "mw-content-text"})
        desc = desc.find("div", {"class": "mw-parser-output"}, recursive=False)
        paragraphs = desc.find_all("p", {'class': None}, recursive=False)

        summary = ""
        if paragraphs != None: 
            for p in paragraphs:
                if p.find("aside") == None: # remove the dumb aside
                    summary = summary + p.text
            if summary == "": #no summary
                print("Skipping: Could not paarse Summary!")
            else: 
                #print(summary)
                summary = nltk.sent_tokenize(summary)

        # add to knowlage base
        if summary != "" and title != None:
            knowledge_base[title] = {
                'link': starter_url,
                'summary': summary[:10]
            }
    except:
        print("Could not Parse!")
    if depth <= 0: 
        return
    
    visited_urls.append(parent_url_parse.netloc+parent_url_parse.path)
    #find and visit child urls
    counter = 0
    
    alllinks = soup.find_all('a')
    print(len(alllinks))
    random.shuffle(alllinks)
    # find urls
    for link in alllinks:
        href = link.get('href')
        if href and (href.startswith("http") or not href[0] == "#"):
            
            #normalise URL
            href = urllib.parse.urljoin(domain, href)
            url_parse = urlparse(href)
            cur_domain = url_parse.netloc
            
            

            if cur_domain != domain: # we want to stay within our domain
                print("Skipping: Not in our domain!")
                continue
            
            
            url, res = visit_url(href)
            if res == None: # tere was an error visiting the url
                print("Skipping: Error visiting!")
                continue
            
            
            print(url)
            
            # summary_container = soup.find("div", {"id": "mw-content-text"})
            # if summary_container == None:
            #     continue
            # summary = None
            # for paragraphs in summary_container.find_all("p"):
            #     if paragraphs.get("class") == None:
            #         summary = paragraphs.getText()
            #         break 
            # if summary == None: # no summary
            #     continue
            # summary = soup.find("meta", {"property": "og:description"})
            # if summary == None: # no summary
            #      continue
            # summary = summary.get("content")
            # summary = re.sub('[^A-Za-z0-9 .,\'\"!()[]{*}$%^]+', '', summary)

            
            # try:
            #     wikipage = wikia.page("harrypotter", "Harry Potter")
            #     title = wikipage.title
            #     summary = wikipage.summary
            # except: # was an issue getting content.  Delete
            #     break
            
            
            

            # Recurce down the link tree
            
            _crawl(url, depth-1, link_limit)
            
            
            
        #print(link.get('href'))
            if counter > link_limit: #limit search at 1000 links
                break
            counter += 1

    






# handles common visit tasks
def visit_url(url: str):    
    re = None
    try:
        re = requests.get(url)
    except:
        return url, None
    o = urlparse(url)

    #check for redirects
    if "wikipedia" in o.netloc: # wikipedia is dumb and has a special way of doing url redirects
        soup = BeautifulSoup(re.text, features="html.parser")

        for link in soup.find_all("link"):
            rel = link.get('rel')
            if rel:
                rel = rel[0]
                if rel == "canonical":
                    url = link.get('href')
                    break

    else:
        url = re.url
    
    #remove anchors
    index = url.find("#")
    if index != -1: 
        url = url[:index]
    print(url)
    return url, re




if __name__ == '__main__':
    main()