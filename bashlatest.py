#!/usr/bin/python
# Licensed under GPL 3.0
# By Daan van Vugt <daanvanvugt@gmail.com>
# Depends on PyRSS2Gen from http://www.dalkescientific.com/Python/PyRSS2Gen.html
# And Beautiful Soup

import sys
import re
import datetime
import PyRSS2Gen as RSS2
from BeautifulSoup import BeautifulSoup

getNumber = re.compile('<b>#(.*)</b>')


quotes = [] # For the rss feed

bash = BeautifulSoup(''.join(sys.stdin.readlines()))

for data, quote in zip(bash('p', 'quote'), bash('p', 'qt')):
    text = ""
    for line in quote:
        line = unicode(line)#.encode('iso-8859-1')
        if line != '<br />' and line.strip() != '':
            text = text + line.strip() + "<br />\r\n"
    num = getNumber.search(unicode(data)).group(1)

    quotes.append(RSS2.RSSItem(title = unicode(data.b.string),
        link = 'http://bash.org?'+num,
        description = text,
        guid = 'http://bash.org?'+num))



#generate feed
rss = RSS2.RSS2(
    title = "Bash.org Latest Quotes",
    link = "http://www.bash.org?latest",
    description = "Bash.org 50 Latest Quotes",

    lastBuildDate = datetime.datetime.now(),

    items = quotes)


print rss.to_xml('iso-8859-1')

