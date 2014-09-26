#!/usr/bin/python
# Andrew getData.py Version 1.0
# Created April 8, 2014
# Updated April 8, 2014

import csv
import httplib2
import cStringIO
import urllib
import xml.etree.cElementTree as et

# Get financial data from morningstar.com

def get_ms_data(symbol, type):
    h = httplib2.Http('.cache')
    url = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=' + symbol + '&region=USA&culture=en_us&reportType=' + type +'&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&productCode=usa&r=283305&denominatorView=raw&number=3'
    headers, data = h.request(url)
    msdatacsv = cStringIO.StringIO(data)
    msdata = csv.reader(msdatacsv)
    return msdata


# Get stock data from yahoo finance
# See complete list of yahoo finance code here: https://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty

def get_yf_data(symbol, code):
    h = httplib2.Http('.cache')
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=' + symbol + '&f=s' + code
    headers, data = h.request(url)
    yfdatacsv = cStringIO.StringIO(data)
    yfdata = csv.reader(yfdatacsv)
    for row in yfdata:
        if len(row) >= 2:
            return row[1]
            break
        else:
            return "N/A"
            break
            
# Get the number of clinical trials of a particular phase and a particular status
## Phases: 1, 2, 3
## Status: "Open", "Recruiting", "Active+not+recruiting", "Completed"

def get_ct_count(company, phase, status):
    phase = str(phase - 1)
    company = urllib.quote(company)
    h = httplib2.Http('.cache')
    url = 'http://clinicaltrial.gov/ct2/results?recr=' + status + '&spons=' + company + '&phase=' + phase + '&displayxml=true'
    headers, data = h.request(url)
    root = et.fromstring(data)
    count = root.attrib['count']
    return count
            
