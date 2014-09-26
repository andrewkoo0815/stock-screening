#!/usr/bin/python
# Andrew backend.py Version 1.0
# Created April 8, 2014
# Updated April 8, 2014


import get_data

# Create a list of data for each company
def generateDataList(symbol, company):
    
    # Get stock data from yahoo finance
    marketcap = "$" + str(get_data.get_yf_data(symbol, "j1"))
    price = "$" + str(get_data.get_yf_data(symbol, "p0"))
    ptarget = "$" + str(get_data.get_yf_data(symbol, "t8"))
    volume = get_data.get_yf_data(symbol, "v0")
    sharesout = str(get_data.get_yf_data(symbol, "j2")) + " M"
    
    # Get financial data from Morningstar
    isdata = get_data.get_ms_data(symbol, "is")
    bsdata = get_data.get_ms_data(symbol, "bs")
    
    # Set default if the value is none or not available
    latestq = "N/A"
    tocash = "N/A"
    tolia = "N/A"
    rev = "No Revenue"
    growth = "N/A"
    costrev = "N/A"
    qexp = "N/A" 
    star = "No"
    
    # Get clinical trial data from clinicaltrial.gov
    
    # Phase II Completed
    count1 = get_data.get_ct_count(company, 2, "Completed")
    # Phase III Completed
    count2 = get_data.get_ct_count(company, 3, "Completed")
    # Phase III Ongoing
    count3 = get_data.get_ct_count(company, 3, "Open")
    
    # Get Total Cash and Total Liability from the Balance Sheet
    row_count = 0    
    for row in bsdata:
        if row[0] == "Total cash":
            tocash = "$" + str(row[5]) + " M"
        elif row[0] == "Total liabilities":
            tolia = "$" + str(row[5]) + " M"
            break
        row_count += 1
    
    # Get Total Revenue, Revenue Growth, Cost of Revenue, and Operating Expense from the Income Statement
    row_count = 0    
    for row in isdata:
        if row_count == 1:
            latestq = row[5]
        elif row[0] == "Revenue":
            if (row[4] == "0" and row[5] != ""):
                  rev = "$" + str(row[5]) + " M"
                  growth = "1st Q w/ Rev"
            elif (row[4] == "-0" and row[5] != ""):
                  rev = "$" + str(row[5]) + " M"
                  growth = "1st Q w/ Rev"
            elif (row[4] != "" and row[5] != ""):
                  rev = "$" + str(row[5]) + " M"
                  growth = "{0:.0f}%".format(100*float(row[5])/float(row[4])-100)
                  # Pick for stock with the "Star" status
                  if float(row[4]) >= float(10) and float(row[5])/float(row[4]) >= 1.25:
                        star = "Yes"                  
        elif row[0] == "Cost of revenue":
            costrev = "$" + str(row[5]) + " M"
        elif row[0] == "Total operating expenses":
            qexp = "$" + str(row[5]) + " M"
            break
        row_count += 1
    
    dataset = [company, symbol, price, ptarget, marketcap, volume, sharesout, latestq, tocash, tolia, rev, growth, costrev, qexp, star, count1, count2, count3]
    return dataset

# Define the name corresponding to the dataset
def generate_column_name():
 	
 	columnlist = ["Company", "Symbol", "Price", "1 yr Target", "Mkt Cap", "Volume", "Shares Out", "Latest Q", "Total Cash", "Total Liability","Q Revenue" ,"Q Growth", "Cost of Rev", "Q Expense", "Star", "PII Completed", "PIII Completed", "PIII Ongoing"]
 	return columnlist
