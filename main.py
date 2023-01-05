import  boto3
import schedule
ec2_client=boto3.client('ec2' )
ec2_resource= boto3.resource('ec2')

reservations=ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances=reservation['instances']
    for instance in instances:
       print(f"Instance {instance['instanceId']} is {instance['State']['Name']} ")

def check_instance_status():

    statuses=ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses["InstanceStatuses"]:
        ins_status = status['instanceStatus']['Status']
        sys_status= status['SystemStatus']['Status']
        state=status['InstanceState'] #can get the above for loop easily in this line
        print(f"Instance {status['InstanceId']} status is {ins_status} and system status is {sys_status}")
    print("###########################")

schedule.every(5).minutes.do(check_instance_status())
while True:
    schedule.run_pending()