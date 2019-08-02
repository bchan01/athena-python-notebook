# Jupyter Notebook and AWS Athena

## Data Retrievals

1. Get data from Yahoo

2. cleanup data - python parse.py

3. Upload data to S3 Bucket

4. Create Athena Database

5. Create Athena Table pointing to the S3 Bucket

6. Run few queries in Athena

## Launch Python Notebook

1. Build Jupyter Notebook Docker Image
```
docker build --no-cache -t scipy-athena:dev .
```

2. Launch Jupyter Notebook using Docker-Compose

```
update .env with your AWS credentials
docker-compose down
docker-compose build --no-cache
docker-compose up
```

3. Connect to Athena and perform Data explorations
