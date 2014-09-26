#!/usr/bin/python
# Andrew import_symbols.py Version 1.0

from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
import datetime
import csv
import os; os.chdir('/Users/andrewkoo/Workspace/Stock_screening/')


def import_industry_tickers(url):
	
	html = urlopen(url).read()
	symbolsoup = BeautifulSoup(html, "lxml")
	
	symbolmaterial = []
	links = [a.string for a in symbolsoup.findAll("a")]
	
	status = False
	for i in range(len(links)):
		if (links[i] == "Private / Foreign"):
			status = True
		elif (links[i] == "What's This?"):
			status = False
		elif (status == True):
			symbolmaterial.append(links[i].encode('utf-8'))
	
	symbolmaterial = symbolmaterial[:-3]
	
	return symbolmaterial		


def write_events():
	
	companies = {}
	
	urllist = []

	urllist.append("http://biz.yahoo.com/ic/510_cl_pub.html") # Drug Manufacturer
	urllist.append("http://biz.yahoo.com/ic/511_cl_pub.html") # Other Drug Manufacturer
	urllist.append("http://biz.yahoo.com/ic/512_cl_pub.html") # Generic
	urllist.append("http://biz.yahoo.com/ic/513_cl_pub.html") # Drug Delivery
	urllist.append("http://biz.yahoo.com/ic/514_cl_pub.html") # Drug Related Products
	urllist.append("http://biz.yahoo.com/ic/515_cl_pub.html") # Biotechnology
	urllist.append("http://biz.yahoo.com/ic/516_cl_pub.html") # Diagnostic
	
	for i in range(len(urllist)):
		symbolmaterial = import_industry_tickers(urllist[i])
		for j in range(len(symbolmaterial)/2):
			companies[symbolmaterial[2*j + 1]] = symbolmaterial[2*j]

	
	symbollistcsv = open('Files/symbol_list_'+ time.strftime("%Y%m%d") + '.csv', 'wb')
	symbol_list_writer = csv.writer(symbollistcsv)
	
	companylist = sorted(companies.keys(), key=str.lower)
	
	for k in range(len(companylist)):
		symbol_list_writer.writerow([companylist[k], companies[companylist[k]]])
	
	symbollistcsv.close()



def main():
	# Import all FDA events from FDA calendar
	write_events()
	print "Event Import Complete"
   	

if __name__ == '__main__':
	main()
