import boto3

ec2_client=boto3.client('ec2')
ec2_resource= boto3.resource('ec2')

ec2_client_paris=boto3.client('ec2')
ec2_resource_paris= boto3.resource('ec2')

insatance_ids=[]
instance_ids_paris=[]
reservations=ec2_client.describe_instances()["Reservations"]
reservations_paris=ec2_client_paris.describe_instances()["Reservations"]
for res in reservations:
    instance =res['Instances']
    for ins in instance:
        insatance_ids.append(ins['InstanceId '])

response =ec2_resource.create_tags(
    Resources=insatance_ids,
    Tags=[
        {
            'key':'environment',
            'Value':'prod'
        },
    ]
)

for res in reservations:
    instance =res['Instances']
    for ins in instance:
       instance_ids_paris.append(ins['InstanceId '])

response_paris =ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tags=[
        {
            'key':'environment',
            'Value':'dev'
        },
    ]
)