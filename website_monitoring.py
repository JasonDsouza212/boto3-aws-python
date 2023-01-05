import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
def send_notification(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = message
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


try:
    response = requests.get("http://ec2-3-111-187-240.ap-south-1.compute.amazonaws.com:8080")
    if response.status_code == 200:
        print("Everythings ok ")
    else:
        print("Server crashed")
        send_notification("Subject:SITE DOWN\n FIX THE ISSUE")

        #restart the app
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='43.205.177.33',username='ec2-user',key_filename='/Users/jason/.ssh/id_rsa')
        stdin,stdout,stderr=ssh.exec_command('docker start image_id')
        print(stdout.readlines())
        ssh.close()
except Exception as ex:
   print(f'Connection  error happend: {ex}')
   send_notification( "Subject:SITE DOWN\nApp not accessible at all FIX THE ISSUE")