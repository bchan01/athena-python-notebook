import gzip
symbols = ['AAPL', 'COF', 'GOOG', '^GSPC']
input = 'data/raw/'
staging = 'data/processed/'
output = 'data/gzip/'
for symbol in symbols:
    out_file = open(staging + symbol + '.csv', 'w')
    line_count = 0
    with open(input + symbol + '.csv', 'r') as file:
        for line in file:
            if line_count > 0:
                line = line.strip()
                line = symbol + "," + line
                if line_count > 1:
                    out_file.write('\n')
                out_file.write(line)
            line_count += 1
    out_file.close()

for symbol in symbols:
    with open(staging + symbol + '.csv', 'rb') as f_in, gzip.open(output + symbol + '.csv.gz', 'wb') as f_out:
        f_out.writelines(f_in)
