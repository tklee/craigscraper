#!/usr/bin/python
# searchterm is the first argument after the program name
import sys
import re, urllib2, urllib

searchterm = sys.argv[1]
htmlpage = urllib2.urlopen("http://sfbay.craigslist.org/cps/").read()
alllinks = re.findall('<a href=.*?>(.*?)</a>', htmlpage)
#alllinks = re.findall('<title>.*?</title>', htmlpage)
count = 0

for links in alllinks:
	if searchterm in links: 
		#urllib.urlretrieve(links, "file-%d.html"%count)
		print links
		count += 1
