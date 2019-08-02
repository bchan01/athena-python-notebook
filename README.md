# Visualizing AWS Athena Data in Jupyter Notebook

## Data Retrievals

1. Download a few historical stock price CSV files from Yahoo Finance

2. Cleanup the file data and GZIP the file
```
python process.py
```
3. Upload GZIP files to S3 Bucket

4. Create Athena Database (database name: mydatabase)

5. Create Athena Table pointing to the S3 Bucket (table name: historical_stock_price)

6. Run few queries in Athena for verifications

```
select count(*) from mydatabase.historical_stock_price where symbol = 'GOOG' 
select * from mydatabase.historical_stock_price where symbol = 'GOOG' and trade_date > date('2019-07-20')
```

## Build and launch Jupyter Notebook

1. Build Jupyter Notebook Docker Image
```
docker build --no-cache -t scipy-athena:dev .
```

2. Launch Jupyter Notebook using Docker-Compose

** Create .env file and update your AWS Credentials
```
AWS_ACCESS_KEY_ID=YOUR KEY
AWS_SECRET_ACCESS_KEY=YOUR SECRET
AWS_REGION=YOUR REGION
AWS_S3_STAGING=YOUR S3 STAGING BUCKET (NOT THE SAME AS YOUR DATA S3 Bucket!!)
```

```
update .env with your AWS credentials
docker-compose down
docker-compose build --no-cache
docker-compose up
```

3. Connect to Athena and perform Data explorations
