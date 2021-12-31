import pandas as pd
import json

df = pd.read_excel('capitals.xls')
print(df['Country'], df['Capital City'])
capital_dict = {}

for i in range(len(df['Country'])):
    if type(df['Country'][i]) != float:
        capital_dict[df['Country'][i].strip()] = df['Capital City'][i].strip()
        print(df['Country'][i], df['Capital City'][i])

x = json.dumps(capital_dict)
print(x)
