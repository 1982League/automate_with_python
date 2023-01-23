#!/usr/bin/python3

"""
Automate with Python 
Panda library reading CSV content from the link and storing in a variable and rename the columns.
"""

import pandas as pd

df_2022 = pd.read_csv('https://football-data.co.uk/mmz4281/2223/E0.csv')
print(df_2022)

df_2022.rename(columns={
                         'FTHG': 'Home_Goals',
                         'FTAG': 'Away_Goals'
                         }, inplace=True)

print(df_2022)
