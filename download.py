from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

now_time = datetime.now()
start_time = datetime(now_time.year - 5, now_time.month, now_time.day)
symbol = 'COF'
stock_df = web.DataReader(symbol, 'yahoo', start_time, now_time)
output_name = symbol + '.csv'
stock_df.to_csv(output_name)
