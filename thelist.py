#!/usr/bin/env python

import argparse
from lxml import html
import requests

parser = argparse.ArgumentParser(description='simple python script to view sf bay area concerts')
parser.add_argument('-d', help='Day of the week', required=False)
args = parser.parse_args()

page = requests.get('http://www.foopee.com/punk/the-list/by-date.0.html')
tree = html.fromstring(page.content)
dates = tree.xpath('//li/a/b/text()')

def f(x):
	return {
		'mon': 0,
		'tue': 1,
		'wed': 2,
		'thu': 3,
		'fri': 4,
		'sat': 5,
		'sun': 6,
	}[x]

#for date in dates:
if(args.d == None):
	for date in dates:
		i = dates.index(date) + 1
		venues = tree.xpath('(//ul//ul)[%d]//*[1]//a[contains(@href, "by-club")]//text()' % i)
		shows = tree.xpath('(//ul//ul)[%d]//a//text()' % i)
		print "#################################################"
		print date
		print "#################################################"
		for venue in venues:
			j = venues.index(venue) + 1
			bands = tree.xpath('(//ul//ul)[%d]//*[%d]//a[contains(@href, "by-band")]/text()' % (i, j))
			print venue
			print "-------------------------------------------------"
			for band in bands:
				print "* " + band
			print "\n"
else:
	i = f(args.d)
	date = dates[i - 1]
	venues = tree.xpath('(//ul//ul)[%d]//*[1]//a[contains(@href, "by-club")]//text()' % i)
	shows = tree.xpath('(//ul//ul)[%d]//a//text()' % i)
	print "#################################################"
	print date
	print "#################################################"
	for venue in venues:
		j = venues.index(venue) + 1
		bands = tree.xpath('(//ul//ul)[%d]//*[%d]//a[contains(@href, "by-band")]/text()' % (i, j))
		print venue
		print "-------------------------------------------------"
		for band in bands:
			print "* " + band
		print "\n"