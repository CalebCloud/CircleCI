import boto3
from flask import Flask
app = flask(__name__)

@app.route("/")
def main():
    key_id = input('Enter your AWS access key credentials.')
    secret_key_id = input('Enter your AWS secret access key credentials.')
    bucket_name = input('What do you want the name of the bucket to be?')
    object_name = input('What do you want S3 file to be named?')
    object_name = (str(object_name) + '.txt')
    object_content = input('What do you want the s3 file to say?')
    object_link = (f'https://{bucket_name}.s3-us-west-2.amazonaws.com/{object_name}')

    client = boto3.client(
        's3',
        aws_access_key_id = key_id,
        aws_secret_access_key = secret_key_id
    )

    client.create_bucket(
        ACL = 'public-read-write',
        Bucket = bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2'
        }
    )

    client.put_object(
        Body = object_content,
        Bucket = bucket_name,
        Key = object_name,
        ACL='public-read',
        ContentType='media-type'
    ) 
    return(f'The link to your file {object_link}!')

if __name__ == "__main__":
    app.run

def Add(a, b):
    return a + b
