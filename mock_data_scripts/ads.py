import random, os
from mysql.connector import connect
import boto3
# AWS S3 Client
s3 = boto3.client(
    's3', 
    aws_access_key_id    = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name          = os.environ.get("AWS_REGION"),
	)

conn = connect(
	host =os.environ.get("RDS_MYSQL_HOST"),
	port =os.environ.get("RDS_MYSQL_PORT"),
	user =os.environ.get("RDS_MYSQL_USER"),
	password =os.environ.get("RDS_MYSQL_PASSWORD"),
	database = os.environ.get("RDS_MYSQL_DATABASE"),
	) 



response = s3.list_objects_v2(Bucket='fuel-bucket-001', Prefix='ads/')
# Extract all object keys
keys = [obj['Key'] for obj in response.get('Contents', [])]
url = 'https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/'
list_url = [url + key for key in keys]


cursor = conn.cursor()
i = 1
for url in list_url:
    x = '"'+url+ '"'
    query  = "INSERT INTO ads(ad_image) values( "+ x +");"
    print(query)
    cursor.execute(query)
    conn.commit()
    i = i + 1
conn.close()