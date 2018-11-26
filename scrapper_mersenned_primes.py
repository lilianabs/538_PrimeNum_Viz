#!/usr/bin/python

"""
Created on Tue Jan 16 14:38:47 2018
@author: liliana

This script downloads the main table from 
https://www.mersenne.org/primes/ and saves it in a csv file.
"""

# import libraries
import urllib3
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    
    columns_table = []
    for col in soup.findAll('th'):
        if not col.find(text=True)=='Contestants':
            columns_table.append(col.find(text=True))
    
    table=[]
    #Every row of the table is inside tags <tr> and </td>
    for row in soup.findAll("tr"):
        #Every cell is inside tags <td> and </td>
        cells = row.findAll('td')
        if len(cells)==len(columns_table):
            table.append([cell.find(text=True) for cell in cells])
    
    return pd.DataFrame(table,columns=columns_table)
    


def main(url):
   
    df = get_data(url)    
    #We save the df to a csv file
    df.to_csv("data/prime.csv",index=False)

if __name__ == '__main__':
    #Url of the table
    url = 'https://www.mersenne.org/primes/'
    main(url)


