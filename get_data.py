import gzip
import subprocess
from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

symbols = ['AAPL', 'COF', 'GOOG', '^GSPC']
raw = 'data/raw/'
staging = 'data/staging/'
output = 'data/gzip/'


def download(symbol, start_date, end_date) :
    stock_df = web.DataReader(symbol, 'yahoo', start_date, end_date)
    output_name = raw + symbol + '.csv'
    stock_df.to_csv(output_name)
    return output_name

def process(symbol, file_path) :
    out_file_name = staging + symbol + '.csv'
    out_file = open(out_file_name, 'w')
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line_count == 0:
                line = "Symbol, Date, Open, High, Low, Close, Adjusted_Close, Volume"
            else:
                line = symbol + "," + line.strip()
                out_file.write('\n')
            out_file.write(line)
            line_count += 1
    out_file.close()
    return out_file_name


def main():
    print('Cleaning up old data ...')
    subprocess.call('rm -rf data', shell=True)
    subprocess.call('mkdir data', shell=True)
    subprocess.call('mkdir data/raw', shell=True)
    subprocess.call('mkdir data/staging', shell=True)
    subprocess.call('mkdir data/gzip', shell=True)
    print('Retrieving Historical Stock Prices ...')
    end_date = datetime.now()
    start_date = datetime(end_date.year - 5, end_date.month, end_date.day)
    for symbol in symbols:
        print('Retrieving Historical Stock Prices for {}'.format(symbol))
        raw_file = download(symbol, start_date, end_date)
        print('Stored data in {}'.format(raw_file))
        out_file = process(symbol, raw_file)
        print('Stored cleaned data in  {}'.format(out_file))
        zip_file = output + symbol + '.csv.gz'
        with open(out_file, 'rb') as f_in, gzip.open(zip_file, 'wb') as f_out:
            f_out.writelines(f_in)
        print('Stored final data in Zip file {}'.format(zip_file))


if __name__ == "__main__":
    main()




