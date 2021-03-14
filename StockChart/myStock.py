import pandas
import numpy
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data as web

abev3 = web.DataReader('ABEV3.SA', data_source='yahoo', start='2015-01-01')['Adj Close']
newabev3 = abev3.reset_index()

priceabev3 = []
#for price in abev3:
#    priceabev3.append(price)

dateabev3 = []
for n in range(0,len(newabev3)):
    dateabev3.append(newabev3['Date'][n])
    priceabev3.append(newabev3['Adj Close'][n])

plt.plot(dateabev3, priceabev3)
plt.show()