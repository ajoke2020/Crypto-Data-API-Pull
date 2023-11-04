from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from time import time
from time import sleep
import seaborn as sns
import matplotlib.pyplot as plt


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f6ee6334-d261-47fd-8212-a0fda6a0ff00',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.json_normalize(data['data'])
#print(df)

  

#Adding a "time_stamps" column to record the exact time the
#data is fetched
df['time_stamps'] = pd.to_datetime('now')


def api_runner():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f6ee6334-d261-47fd-8212-a0fda6a0ff00',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  

#Adding a "time_stamps" column to record the exact time the
#data is fetched
df['time_stamps'] = pd.to_datetime('now')
  #creating a csv and adding an else statement that subsequently 
  #adds new data to the csv without creating headers
if not os.path.isfile(r"C:\Users\USER\Documents\data analytics\Data notes\python scripts\API.csv"):
  df.to_csv(r"C:\Users\USER\Documents\data analytics\Data notes\python scripts\API.csv", header='column_names')
else:
    df.to_csv(r"C:\Users\USER\Documents\data analytics\Data notes\python scripts\API.csv", mode= 'a', header=False)

for i in range(3):
#333 is the maximum number of requests that coinmarketcap allows daily
  api_runner()
  print ('API runner completed successfully')
  sleep(15)

# Set float format
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Group by 'name' and select the desired columns
df2 = df.groupby('name', sort=False)[
    ['quote.USD.percent_change_1h',
    'quote.USD.percent_change_24h',
    'quote.USD.percent_change_7d',
    'quote.USD.percent_change_30d',
    'quote.USD.percent_change_60d',
    'quote.USD.percent_change_90d']
].mean()  # Use .mean() or another aggregation function as needed

# Unstack the data
df3 = df2.unstack().reset_index()

# Rename columns
df3.columns = ['name', 'percent_change', 'values']

# Replace the long names with short names
df3['percent_change'] = df3['percent_change'].replace({
    'quote.USD.percent_change_1h': '1h',
    'quote.USD.percent_change_24h': '24h',
    'quote.USD.percent_change_7d': '7d',
    'quote.USD.percent_change_30d': '30d',
    'quote.USD.percent_change_60d': '60d',
    'quote.USD.percent_change_90d': '90d'
})

# Plot with Seaborn
# Define the order of the categories for the hue
hue_order = ['1h', '24h', '7d', '30d', '60d', '90d']
sns.catplot(x='percent_change', y='values', hue='name', data=df3, kind='point')

# Filter data for Bitcoin and plot a line
df7 = df[df['name'] == 'Bitcoin'][['time_stamps', 'quote.USD.price']]
sns.set_theme(style='darkgrid')
sns.lineplot(x='time_stamps', y='quote.USD.price', data=df7)
