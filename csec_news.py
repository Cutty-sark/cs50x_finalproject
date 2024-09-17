# Module for cybersecurity headlines
from nn import Block

class CybersecHeadlines(Block):
    def __init__(self):
        super().__init__("CSEC TODAY")
    
    sourceone = https://feeds.feedburner.com/TheHackersNews



    def gather_data(self):
        self.add_content("Headline 1")
        self.add_content("Headline 2")
        self.add_content("Headline 3")
