# Network News
#### Video Demo:
#### Description: Command line tool that coalates network health, cybersec headlines, p̶a̶t̶c̶h̶ t̶i̶m̶e̶l̶i̶n̶e̶s̶. Extensible - can easily add additional blocks (objects) to report. 

This readme will differ slightly from the usual in that the project plan will be included.

## Summary

A readout of some headlines and network metrics.

The program uses selenium, feedparser, speedtest, psutil among some other
standard packages.

The program is built to be extensible - using nn.py as a "block creator",
it is a simple task to code a "block" and have it called in main without 
obfuscating the code in main.py or in the nn.py. All formatting is dealt
with in nn.py and the execution in main.py

Thanks to https://outage.report and 
https://feeds.feedburner.com/TheHackersNews

for the external data.

## Project Plan

#### Motivation:
Building on a previous CLI project I made called Cappucino. Intended to be used once a day as a quick brief.
Extensiblility will be a big aim and the main improvement over Cappucino, which I will acheive through leveraging Python classes. I hope to do this via JSON file creation for each endpoint.

#### Outline:
The two starting areas- network health, cybersec headlines.

Network health
Current uptime
Current network speed.
Outages of service providers in the past 24 hours.

Cybersec headlines
3 top headlines

_Display:_

In the command line
In blocks                                          _
blocks should be taken from a template. Dividors  |_|
have width fixed, then scale height with line number.


Tick list
- Have python display a persistent command prompt window
- Display greeting
- Display date, time, Location, weather for the day
- Work out how to put this into json readable.
- Display current network speed.
- Display Major Outages last 24 hours.
- Get block /object set up. to repeat


Class
- print out
- source
- limit on size (length)
- universal limit on width
- divisor graphic

NN/
├──main.py            #main script
├── nn.py             # block creator (formatting)
├── network_health.py # Module for network health information
├── csec_news.py      # Module for cybersecurity headlines
└── utils.py          # Additional utilities if needed


