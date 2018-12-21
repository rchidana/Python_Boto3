import boto3

# Create an S3 client
s3 = boto3.client('s3')

src_filename = '/Users/anandr72/Repos/Python_Boto3/S3.py'
dest_filename = 's3.py'
bucket_name = 'chid-bucket'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.

try:
	response = s3.upload_file(src_filename, bucket_name, dest_filename)
	print ("Uploaded File ",src_filename," Successfully on to Bucket : ",bucket_name)
except Exception as error:
	print (error)
