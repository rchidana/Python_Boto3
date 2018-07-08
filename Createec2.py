import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(MinCount=1, MaxCount=1, ImageId='ami-a4dc46db', InstanceType='t2.micro', SecurityGroups=['ACCENTURE_SEC_GROUP'], KeyName='ACCENTURE_KEYS') # create one instance with a t2.micro instance-type
for instance in instances:
  print("waiting for the instance to be running state")
  instance.wait_until_running()
  instance.reload()
  print("Instance id ", instance.id)
  print("Instance state ", instance.state['Name'])
  print("Instance public DNS", instance.public_dns_name)
