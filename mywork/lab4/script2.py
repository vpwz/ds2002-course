import boto3
import requests
#https://ds2002-qnd8mu.s3.amazonaws.com/downloaded.png?AWSAccessKeyId=ASIAXYKJUMWRY2DEG5GV&Signature=L02zvDfu5mxeWwNUgCHIUaUY9bA%3D&x-amz-security-token=FwoGZXIvYXdzEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDMm8sOyqJmOfrL2kgCLEAXdvrJVVdl9IwgrrluVO9Uv2oHYqgzuzezQhbH%2Fox9575BxVLI8%2Fr3YchsowJ1efJ4ExR5XPzk5JCPTt8L3e9rPByy3nxVftYJ0RXaYEU72lLOTcbnKW3WhhnkbNkus9OosGmJLf63zp2wVl2%2Fl5qEu10I9Aw%2Fr%2FRwlwKynH2BZEPFjhJvjz7dAgwmusq7GwoGJWSr3%2BavwKiHxFmZTowS%2BGNdmT0KCXkXHuoBv25vpZEthyAC85%2FF7pYKkUzsJSWhJjfFMo1fXkrgYyLcMtCTeYotptj64Y1YXBvTUdmMvPFqpQx65wHI8LfbuOKjO3Zk3GB%2BErmbrbWw%3D%3D&Expires=1709350816
url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'

response = requests.get(url)
file_name = 'google_logo.png'
with open(file_name, 'wb') as f:
    f.write(response.content)


s3 = boto3.client('s3')
bucket_name = 'ds2002-qnd8mu'
s3.upload_file(file_name, bucket_name, file_name)


url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': file_name},
    ExpiresIn=604800

    )

print(url)
