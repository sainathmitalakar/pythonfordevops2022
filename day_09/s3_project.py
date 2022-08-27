import boto3


s3_obj = boto3.resource('s3')

def show_bucket(s3_obj):
    for bucket in s3_obj.buckets.all():
      print(bucket.name)
def upload_to_s3(s3_obj,bucket_name,file_name,file_path):
    data = open(file_path, 'rb')
    s3_obj.Bucket(bucket_name).put_object(key=file_name,Body=data)
    data.close()

    print("file uploaded successfully")

upload_to_s3(s3_obj,'python-for-devops-12','sainath.txt','my_secrete.txt')