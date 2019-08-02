from pyathena import connect
import pandas as pd
import seaborn
import os

#environment vars
access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
staging = os.environ['AWS_S3_STAGING']
region = os.environ['AWS_REGION']

conn = connect(aws_access_key_id=access_key,
               aws_secret_access_key=secret_key,
               s3_staging_dir=staging,
               region_name=region)



stock_prices = pd.read_sql("select * from mydatabase.historical_stock_price where symbol = 'GOOG'", conn)

stock_prices.tail(3)

import matplotlib.pyplot as plt
from matplotlib import style
df_prices = pd.DataFrame(stock_prices, columns=['close_price'])
df_prices.plot(title='Daily Close Price for GOOG', figsize=(20,10), kind='line')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


import math as math
stock_prices['price_range']=stock_prices['high_price'] - stock_prices['low_price']
df_ranges = pd.DataFrame(stock_prices, columns=['price_range'])
df_ranges.plot(title="Daily Price Range for GOOG", figsize=(20,10), kind='line')
plt.xlabel('Date')
plt.ylabel('Range')
plt.show()



stock_prices['V']=stock_prices['volume']/1000000.0
df_volume = pd.DataFrame(stock_prices, columns=['V'])
df_volume.plot(title='Daily Trading Volume for GOOG', figsize=(20,10), kind='line')
plt.xlabel('Date')
plt.ylabel('Volume (Million)')
plt.show()

