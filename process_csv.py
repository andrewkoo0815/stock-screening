#!/usr/bin/python
# Andrew processCSV.py Version 1.0
# Created April 8, 2014
# Updated April 8, 2014

import csv
import time
import backend

# Load the list of stock symbols
def load_symbol_list():
	stocklistcsv = open('Files/symbol_list.csv', 'rU')
	stock_list = csv.reader(stocklistcsv)
	return stock_list

# Load the last financial quarter from the previous run
def load_old_date_list():
	stock_list = load_symbol_list()
	olddate_list = []
	for row in stock_list:
		olddate_list.append(row[2])
	return olddate_list

# Call backend and write the data into a CSV file
def write_data():
    stock_list = load_symbol_list()
    stockdatacsv = open('Files/stock_data_'+ time.strftime("%Y%m%d") + '.csv', 'wb')
    stock_data = csv.writer(stockdatacsv)
    
    # Get the name of the column from the backend module
    stock_data.writerow(backend.generate_column_name())
    for row in stock_list:
        symbol = row[0]
        company = row[1]
        print "Processing " + symbol
    
        # Get all the data from the backend module
        stock_data.writerow(backend.generateDataList(symbol, company))
    stockdatacsv.close()

# Create a list of stock with the updated financial data and "Star" status, also update the symbol list with the latest quarter
def update_csv(olddate_list):
    stockdatacsv = open('Files/stock_data_'+ time.strftime("%Y%m%d") + '.csv', 'rU')
    stock_data = csv.reader(stockdatacsv)
    symbols, companies, data_date, stars = [], [], [], []
    for row in stock_data:
        symbols.append(row[1])
        companies.append(row[0])
        data_date.append(row[7])
        stars.append(row[14])
    stocklistcsv = open('Files/symbol_list.csv', 'wb')
    stock_list = csv.writer(stocklistcsv)
    updated_list = []
    star_list = []
    star_updated_list = []
    seq = 1
    while seq <= len(symbols) - 1:
        if olddate_list[seq-1] != data_date[seq]:
            updated_list.append(symbols[seq])
            if stars[seq] == 'Yes':
                star_list.append(symbols[seq])
        stock_list.writerow([symbols[seq], companies[seq], data_date[seq]])
        seq += 1     
    return updated_list, star_list
 
