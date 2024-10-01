# Module for cybersecurity headlines
from nn import Block
import feedparser
import requests
import re

class CybersecHeadlines(Block):
    def __init__(self):
        super().__init__("CSEC TODAY")
    



    def gather_data(self):
        #use feedparser to grab data
        thnkeys = feedparser.parse("feeds.feedburner.com/TheHackersNews").keys()
        thnfeed = feedparser.parse("feeds.feedburner.com/TheHackersNews")
        #parser showing nowthing so trying to trouble shoot
        #bozo = 1 if trouble parsing
        if thnfeed.bozo == 1:
            print("parse error")
            print(thnfeed.bozo_exception)

        url = "https://feeds.feedburner.com/TheHackersNews"
        response = requests.get(url)

# Output the raw XML to inspect it
        text = response.content.decode('utf-8', errors='replace')
        print(response.content.decode('utf-8', errors='replace'))  # Replace problematic characters
        titleselector = r'<title>(.*?)</title>'
        
        if 'title' in thnfeed.feed == True:
            print("True")
        titlevector = re.findall(titleselector, text)
        # for i in range(2):
        #    if #string is = title, do until /title
        #       titlevector[i] = #abc
        #       self.add_content(titlevector(i))
        # inspecting the xml, we can look for <title> abc </title>
        # append to titlevector abc
        # for 3 counts.
        # then print the three to the entries. 
        print(len(thnfeed.entries))
        print(titlevector)
        self.add_content(titlevector[2])
        self.add_content(titlevector[3])
        self.add_content(titlevector[4])
        # self.add_content(titlevector[0])
        # self.add_content(titlevector[1])
        # self.add_content()
