import schedule
import time
import boto3


s3_obj = boto3.resource('s3')
def say_hi():
    print("hi sainath")

schedule.every(2).seconds.do(s3_project.show_buckets,s3_obj,say_hi)

while True:
    schedule.run_pending()
    time.sleep(1)