#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:38:47 2018

@author: liliana
"""

# import libraries
import urllib3
from bs4 import BeautifulSoup
import pandas as pd


http = urllib3.PoolManager()

url = 'https://www.mersenne.org/primes/'
response = http.request('GET', url)
soup = BeautifulSoup(response.data, 'html.parser')

columns_table=[]
for col in soup.findAll('th'):
    if not col.find(text=True)=='Contestants':
        columns_table.append(col.find(text=True))

table=[]

for row in soup.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==len(columns_table):
        table.append([cell.find(text=True) for cell in cells])
        
    
df=pd.DataFrame(table,columns=columns_table)
df.to_csv("prime.csv",index=False)