import os
import pandas as pd
cwd = os.path.abspath('./files')
files = os.listdir(cwd)
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel("./files/"+file), ignore_index=True)
df.head()
df.to_excel('total_sales.xlsx')
