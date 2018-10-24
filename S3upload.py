import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'S3.py'
bucket_name = 'chid-bucket'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.

try:
	response = s3.upload_file(filename, bucket_name, filename)
	print ("Uploaded File ",filename," Successfully on to Bucket : ",bucket_name)
except Exception as error:
	print (error)
