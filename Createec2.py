import boto3
ec2 = boto3.resource('ec2')
tags = [
            {'Key':'Name','Value': 'Boto3-EC2'},
            {'Key': 'Department', 'Value': 'Web-Dep'},
        ]
tag_specification = [{'ResourceType': 'instance', 'Tags': tags},]
instances = ec2.create_instances(MinCount=1, MaxCount=1, ImageId='ami-a4dc46db', InstanceType='t2.micro', SecurityGroups=['ACCENTURE_SEC_GROUP'], KeyName='ACCENTURE_KEYS',TagSpecifications=tag_specification) # create one instance with a t2.micro instance-type
for instance in instances:
  print("waiting for the instance to be running state")
  instance.wait_until_running()
  instance.reload()
  print("Instance id ", instance.id)
  print("Instance state ", instance.state['Name'])
  print("Instance public DNS", instance.public_dns_name)
  print("Tagging the instance")
  ec2.Tag(instance.id, 'Name','Boto-Tag')
