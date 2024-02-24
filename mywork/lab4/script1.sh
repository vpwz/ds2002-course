

#!/bin/bash

#https://ds2002-qnd8mu.s3.us-east-1.amazonaws.com/fruit1.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAXYKJUMWRY2DEG5GV%2F20240224%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240224T035453Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDMm8sOyqJmOfrL2kgCLEAXdvrJVVdl9IwgrrluVO9Uv2oHYqgzuzezQhbH%2Fox9575BxVLI8%2Fr3YchsowJ1efJ4ExR5XPzk5JCPTt8L3e9rPByy3nxVftYJ0RXaYEU72lLOTcbnKW3WhhnkbNkus9OosGmJLf63zp2wVl2%2Fl5qEu10I9Aw%2Fr%2FRwlwKynH2BZEPFjhJvjz7dAgwmusq7GwoGJWSr3%2BavwKiHxFmZTowS%2BGNdmT0KCXkXHuoBv25vpZEthyAC85%2FF7pYKkUzsJSWhJjfFMo1fXkrgYyLcMtCTeYotptj64Y1YXBvTUdmMvPFqpQx65wHI8LfbuOKjO3Zk3GB%2BErmbrbWw%3D%3D&X-Amz-Signature=46c16aa7e8b40b4bfc1409cf7b671dc9fd5edce7e6def4f2d3a378266c9beee4
bucket="ds2002-qnd8mu"
file_path="C:/Users/victo/images/fruit1.jpeg"


aws s3 cp $file_path s3://$bucket/


url=$(aws s3 presign s3://$bucket/$(basename $file_path) --expires-in 604800)

echo "Presigned URL: $url"
