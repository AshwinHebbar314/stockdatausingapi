#%%
import requests
import datetime
dataset = []

#%%
tickers = ['AMZN', 'IBM', 'GM', 'GOOGL', 'FDX']
for i in tickers:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + i + '&apikey=Y757ROOTC67QABNT'
    r = requests.get(url)
    data = r.json()
    dataset.append(data)

#%%
# tickers = ['TSLA', 'MA']
# for i in tickers:
#    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + i + '&apikey=Y757ROOTC67QABNT'
#    r = requests.get(url)
#   data = r.json()
#   dataset.append(data)
# %%
f = open('dataset.txt', 'w')
f.write(str(dataset))
f.close()
# %%
import datetime
str(datetime.date(2021,9,10)-datetime.timedelta(7*2))
# %%
len(dataset)
# %%
