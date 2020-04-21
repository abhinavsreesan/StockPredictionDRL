import pandas as pd
from os import listdir
from glob import iglob
import numpy as np

columns = ["TICKER", "DATE", "TIME", "OPEN","HIGH","LOW","CLOSE"]

path = r'D:\Projects\Stock\oneminutedata-20190611T170325Z-001\oneminutedata\**\NIFTY.txt'
all_rec = iglob(path, recursive=True)
dataframes = (pd.read_csv(f,header=None,delimiter=",",usecols=[0,1,2,3,4,5,6],names=columns) for f in all_rec)
big_dataframe = pd.concat(dataframes, ignore_index=True,sort=False)

print(big_dataframe.head())

big_dataframe.to_csv('D:\Projects\Stock\oneminutedata-20190611T170325Z-001\oneminutedata\op.csv',sep=',',index=False)