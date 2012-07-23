#!/usr/bin/python
# searchterm is the first argument after the program name
import sys
import re, urllib2, urllib
import struct
from bs4 import BeautifulSoup
import time


searchterm = sys.argv[1]
htmlpage = urllib2.urlopen("http://sfbay.craigslist.org/cps/").read()
alllinks = re.findall('<a href=(.*?)>.*?</a>', htmlpage)
alllinks2 = re.findall('<a href=.*?>(.*?)</a>', htmlpage)
#alllinks = re.findall('<title>.*?</title>', htmlpage)
count = 0

#for links in alllinks:
#	print links


#for links in range(0, len(alllinks)):
#	if 
unused = 0
for links in alllinks2:
	count += 1
	if searchterm in links: 
		if count == len(alllinks2):
			print "this was the ignored last one"
		else:
		#urllib.urlretrieve(links, "file-%d.html"%count)
			alllinks[count] = alllinks[count].replace('\"', '')
			followedlink = urllib2.urlopen(alllinks[count])
			soup = BeautifulSoup(followedlink)
		#	for tag in soup.recursiveChildGenerator(): # and tag.name in ('title', 'body', 'h2', 'h1'):
		#		printvar = True
		#		name = getattr(tag, "name", None)
		#		#if name is not 'a':
		#		#	unused += 1
		#		if name is not None: # and name not in ('title', 'body', 'h2', 'h1'):
		#			if name in ('a', 'br', 'li'):
		#				printvar = False
		#			if printvar:
		#				print name
		#				unused += 1
		#		elif not tag.isspace():
		#			if printvar:
		#				print tag
			for tag in soup.recursiveChildGenerator(): # and tag.name in ('title', 'body', 'h2', 'h1'):
#				printvar = True
				name = getattr(tag, "name", None)
				#if name is not 'a':
				#	unused += 1
				if name is not None: # and name not in ('title', 'body', 'h2', 'h1'):
			#		if name in ('a', 'br', 'li'):
		#				printvar = False
#					if printvar:
#						print name
					unused += 1
				elif not tag.isspace():
#					if printvar:
					print tag
		time.sleep(6)
