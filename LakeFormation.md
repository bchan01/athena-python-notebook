# Lake Formation 101

Getting Started:
https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started.html

Developer Guide:
https://docs.aws.amazon.com/lake-formation/index.html

## Setting up

https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#create-an-iam-user

* Create Roles
* Create DataLakeAdministrator IAM User
* Create DataLake Users (Analyst, Data Scientist, etc)
* Setup Lake Formation Admin User

## Register S3 Location

## Create Database

* Create a database 
* Grant access to roles and users etc.

## Create and Run Crawler

* Specify S3 Bucket, IAM Roles and the target Database
* Crawler will generate the table based on the data

## Grant Permission for Database and Table

* Grant Permissions to User at table with options of including/excluding certain columns

    * Data Scientist can select all columns of a table

    * Data Analysts can only see a limited set of columns of a table

## Query Data in Athena with Different Users

* Login to AWS Athena as a Data Analyst and query table
* Login to AWS Athena as a Data Scientist and query table