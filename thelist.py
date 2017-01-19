from lxml import html
import requests

page = requests.get('http://www.foopee.com/punk/the-list/by-date.0.html')
tree = html.fromstring(page.content)
dates = tree.xpath('//li/a/b/text()')

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