#!/usr/bin/python
# Andrew main.py Version 1.0
# Created April 8, 2014
# Updated April 8, 2014

import process_csv
import send_email
import os; os.chdir('/Users/andrewkoo/workspace/Stock_screening/')

def main():
    
    # Get and write the data into a CSV file
    process_csv.write_data()
    print "CSV File Writing Complete"
    
    # Prepare the list of stocks with updated information and good investment opportunity, update the symbol list in the mean time
    old_date_list = process_csv.load_old_date_list()
    updated_list, star_list = process_csv.update_csv(old_date_list)
    print "Updated list and Star list generated"
    
    # Send Email to myself
    send_email.send_email(updated_list, star_list)
    print "Email Sent"

if __name__ == '__main__':
	main()
