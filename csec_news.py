# Module for cybersecurity headlines
from nn import Block
import feedparser
import requests

class CybersecHeadlines(Block):
    def __init__(self):
        super().__init__("CSEC TODAY")
    



    def gather_data(self):
        #use feedparser to grab data
        thnkeys = feedparser.parse("feeds.feedburner.com/TheHackersNews").keys()
        thnfeed = feedparser.parse("feeds.feedburner.com/TheHackersNews")
        #parser showing nowthing so trying to trouble shoot
        #bozo =1 if trouble parsing
        if thnfeed.bozo == 1:
            print("parse error")
            print(thnfeed.bozo_exception)

        url = "https://feeds.feedburner.com/TheHackersNews"
        response = requests.get(url)

# Output the raw XML to inspect it
        print(response.content.decode('utf-8', errors='replace'))  # Replace problematic characters
        if 'title' in thnfeed.feed == True:
            print("True")
        else:
            print("False")
        print(thnkeys)
        print(thnfeed.entries)
        print(len(thnfeed.entries))
        self.add_content("Headline 1")
        self.add_content("Headline 2")
        self.add_content("Headline 3")
