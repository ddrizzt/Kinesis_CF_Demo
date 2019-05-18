import sys
import boto3
import datetime
import csv
import random
import time

stream_name = sys.argv[1]

print "Load local rating data and send to Kinesis Stream: %s" % stream_name

client = boto3.client(
    'kinesis',
    aws_access_key_id='ACCKEY',
    aws_secret_access_key='SECKEY',
    region_name='ap-southeast-1'
)

resp = client.list_streams()
# stream_name = resp['StreamNames'][0]
stream_name = 'bookrating'
partitionkey = 'PK-01'

with open('./ratings.csv') as csvfile:
    batchnum = 0
    total_send = 0
    batch_count = 1000
    sleep_millsec = 1000
    lc = batch_count
    lines = []
    print

    reader = csv.DictReader(csvfile)
    ts_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    for row in reader:
        lc -= 1
        total_send += 1
        ll = "%s,%s,%s,%s" % (ts_now, row['user_id'], row['book_id'], row['rating'])
        lines.append(ll)

        if lc == 0:
            batchnum += 1
            data_body = "\n".join(lines)
            # Put records to Kinesis stream...
            resp = client.put_record(StreamName=stream_name, Data=data_body, PartitionKey=partitionkey)
            print "%s >>> Batch %s, rows %s, sleep %s, Total_send %s, Data lengh(%s) RESP: %s" % (ts_now, batchnum, batch_count, sleep_millsec, total_send, len(data_body), resp)

            time.sleep(float(sleep_millsec) / 1000)
            batch_count = random.randint(5000, 20000)
            sleep_millsec = random.randint(1500, 3000)
            lc = batch_count
            lines = []
            ts_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

csvfile.close()

sys.exit(0)
