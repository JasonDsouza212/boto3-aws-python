import boto3
import schedule

ec2_client =boto3.client('ec2')

def create_volume_snappshots():
    volumes =ec2_client.describe_volumes(
        Filters=[
            {
                'Name':'tag:Name',
                'Values':['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot =ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)
schedule.every(1).day.do(create_volume_snappshots)

while True:
    schedule.run_pending()