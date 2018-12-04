# /usr/bin/env python

# written by Bhanuprakash Suravarapu
# Description: This Script Starts and Stops the Existing AWS instances
# version 1.0
"""stop and start
Usage:
  Start_and_stop_instance.py start [--name=<instance_name>]
  Start_and_stop_instance.py stop [--name=<instance_name>]
"""
import boto3
import sys
import boto3.ec2
import time
from docopt import docopt

def main(arguments):
    if arguments['start']:
        startInstance(
            arguments['--name']
        )
    elif arguments['stop']:
        stopInstance(
            arguments['--name']
        )

ec2 = boto3.client('ec2')
resource = boto3.resource('ec2')

def startInstance(I_NAME):
    ec2 = boto3.client('ec2')
    resource = boto3.resource('ec2')
    print("Starting the instance...")
    RI_ID = None
    instance = [i for i in resource.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [I_NAME]}, {'Name': 'instance-state-name', 'Values':['stopped']}])]
    for i in instance:
        RI_ID = i.id
    if RI_ID != None:
        print("\nPlease wait while " + I_NAME + " is being started")
        
    else:
        print("\nSeems somthing is wrong..failed..")
        sys.exit(1)

    # change instance ID appropriately  
    
    try:
        ec2.start_instances(
            InstanceIds=[
                RI_ID,
            ],
            DryRun=False
        )
    except:
        print("\nFailed because of wrong input. Please recheck and try")
        sys.exit(1)

    for server in instance:
        while server.state['Name'] not in ('running'):
            print("Please wait...")
            time.sleep(5)
            server.load()
        print('\nInstance is ready to use. Login using private ip: ',server.private_ip_address)

def stopInstance(I_NAME):
    ec2 = boto3.client('ec2')
    resource = boto3.resource('ec2')
    print("Stopping the instance...")
    RI_ID = None
    instance = [i for i in resource.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [I_NAME]}, {'Name': 'instance-state-name', 'Values':['running']}])]
    for i in instance:
        RI_ID = i.id
    if RI_ID != None:
        print("\nPlease wait while " + I_NAME + "is being stopped")
    else:
        print("\nSeems somthing is wrong..failed..")
        sys.exit(1)


    # change instance ID appropriately  
    try:
        ec2.stop_instances(
            InstanceIds=[
            RI_ID,
            ],
            DryRun=False
            )
        print("Instance "+ I_NAME +" stopping.")
    except:
        print("\nFailed because of wrong input. Please recheck and try")
        sys.exit(1)

    for server in instance:
        while server.state['Name'] not in ('stopped'):
            print("Please wait...")
            time.sleep(5)
            server.load()
        print('\nInstance ' + I_NAME + ' stopped. Start instance to continue.')



if __name__ == '__main__':
    arguments = docopt(__doc__, version='launch 1.0')
    main(arguments) 
