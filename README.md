# Network News
#### Video Demo:
#### Description: Command line tool that coalates network health, cybersec headlines, patch timelines. Extensible - can easily add additional blocks (objects) to report. 

This readme will differ slightly from the usual in that the project plan will be included.

## Project Plan

#### Motivation:
Building on a previous CLI project I made called Cappucino. Intended to be used once a day as a quick brief.
Extensiblility will be a big aim and the main improvement over Cappucino, which I will acheive through leveraging Python classes. I hope to do this via JSON file creation for each endpoint.

#### Outline:
The three starting areas, network health, cybersec and dev headlines, and patch timelines.

Network health
Local network outages past 24 hours.
Current network speed.
Outages of major broadband providers past 24 hours.
Top outages of all hosts/providers past 24 hours

Cybersec headlines
3 sources
something funny
links


Patch timelines:
Windows
Topdesk
Microsoft Office
links
coming up this week
Vendor, patch number, release date brief description

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
- Wor

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
├── patch_calendar.py # Module for patch timelines
├── block_template.py # Template and utility functions for formatting
└── utils.py          # Additional utilities if needed


