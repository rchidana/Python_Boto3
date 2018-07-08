import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-25f9f86e']) #Specify your Security Group ID
    print(response)
except ClientError as e:
    print(e)
