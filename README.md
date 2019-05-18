# Kinesis_CF_Demo
Kinesis_CF_Demo, use Cloudformation to initialize the AWS resource.

#############################################

#AWS Structure:
EC2(Send bookrating testing stream data) --> Kinesis --> Firehose --> s3 --> Redshift --> Granfana(Same ec2)

User bookrating data structure: 2 tables, books and rating.

#############################################

Things need be updated:
1. Confirm the region setting is correct in the cf_datastream.json / send_rating_data.py
2. Confirm the S3 bucket path is correct in these files: cf_datastream.json / dbinit.sql 
3. Package the project path to S3. For example:  s3://eason686hm/demos/datastream/code/Kinesis_CF_Demo.tar.gz
4. Create a lambda function and change the cf_datastream.json file as well.

