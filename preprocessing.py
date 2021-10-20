# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
dataset= pd.read_csv('data.csv')

df = pd.DataFrame(dataset)

#dataframe forgets about NA rows
df = df[ df['down'].notna()]
#print(df)

df.to_csv(r'C:\Users\aclav\OneDrive\Desktop\CS368\newdata.csv', index = False, header=True)