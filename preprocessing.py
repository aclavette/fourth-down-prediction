import pandas as pd

dataset= pd.read_csv('data.csv')
df = pd.DataFrame(dataset)

#dataframe forgets about NA rows
df = df[ df['down'].notna()]
df.to_csv(r'C:\Users\aclav\OneDrive\Desktop\CS368\newdata.csv', index = False, header=True)
