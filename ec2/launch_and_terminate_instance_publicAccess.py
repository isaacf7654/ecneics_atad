# /usr/bin/env python
# written by Bhanuprakash Suravarapu
# Updated by Austin Privett
# Description: This Script launches new instance and terminates instances along with Snapshots.
# version 1.0 (+1, AP)
"""launch and terminate
Usage:
  launch_and_terminate_instance.py launch [--image=<image_name>] [--type=<instance_type>] [--name=<instance_name>] [--user=<user>] [--publickey=<key_file>] [--snapshot=<snapshot_name>] [--size=<volume_size>]
  launch_and_terminate_instance.py terminate [--instance=<instance_name>] [--snapname=<snapshot_name>]  
"""

print('''Bhanu says:
         1.  This instance is only for software installations and updates.
         2.  Do not load client data into this instance.
         3.  You can use same AMIs and snapshots to create your instance.
         4.  Let me know before you terminate this instance I will create AMI out of it. (So you do not lose your work).''')

import boto3
from docopt import docopt
import boto3.ec2
import time
import sys

def main(arguments):
    if arguments['launch']:
        create(
            arguments['--image'],
            arguments['--type'],
            arguments['--name'],
            arguments['--user'],
            arguments['--publickey'],
            arguments['--size'],
            arguments['--snapshot'],
        )
    elif arguments['terminate']:
        terminate(
            arguments['--instance'],
            arguments['--snapname']
            
        )

ec2 = boto3.resource('ec2')

def create(IMAGE_NAME,I_TYPE,INSTANCE_NAME,USER,KEY_NAME,EBS,SNAP_NAME=None):
    # Get AMI from tag

    file1 = open(KEY_NAME,'r')
    key = file1.read()

    user_data_script = """#!/bin/bash
    sudo yum update -y
    sudo mkfs.ext4 /dev/xvdh
    sudo mkdir /vol
    echo "/dev/xvdh /vol auto noatime 0 0" | sudo tee -a /etc/fstab
    mount --all
    adduser %s
    groupadd Datawrangler
    usermod -a -G Datawrangler %s
    echo "## Datawrangler user group is allowed to execute halt and reboot" >> /etc/sudoers
    echo -e "%%Datawrangler ALL=NOPASSWD: /sbin/halt, /sbin/reboot, /sbin/poweroff" >> /etc/sudoers
    mkdir /home/%s/.ssh
    chmod 700 /home/%s/.ssh
    chown  %s.%s /home/%s/.ssh
    touch /home/%s/.ssh/authorized_keys
    chown  %s.%s /home/%s/.ssh/authorized_keys
    echo "ssh$%s" | tee -a /home/%s/.ssh/authorized_keys
    """ % (USER, USER, USER, USER, USER, USER, USER, USER, USER, USER, USER, key, USER)

    file1.close()


    AMI = ec2.images.filter(
            Filters=[
           {
               'Name': 'tag:Name',
               'Values': [
               IMAGE_NAME,
               ]
            },
        ],
    )

    for i in AMI:
        IMAGE = i.id


    if(SNAP_NAME ==  None):
        createinstance = ec2.create_instances(
           BlockDeviceMappings=[
              {
                  'DeviceName': '/dev/xvdh',
                  'VirtualName': 'ephemeral',
                  'Ebs': {
                      'Encrypted': True,
                      'DeleteOnTermination': False,
                      'VolumeSize': int(EBS),
                      'VolumeType': 'gp2'
                  },
             },
           ],
           ImageId=IMAGE,
           InstanceType=I_TYPE,
           KeyName= 'localkeypairnonprod',
           MaxCount=1,
           MinCount=1,
           SecurityGroupIds=[
              'sg-0a00f1371e5e23fc8',
           ],
           SubnetId='subnet-033274069137eafae',
           UserData=user_data_script,
           TagSpecifications=[
              {
               'ResourceType': 'instance',
               'Tags': [
                    {
                       'Key': 'Name',
                       'Value': INSTANCE_NAME
                    },
                   ]
             },
           ],
     
        )
    else:
        #This part take care of snaptag to id

        snapshot_iterator = ec2.snapshots.filter(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': [
                        SNAP_NAME,
                    ]
                },
           ],    
        )

        for j in snapshot_iterator:
            SNAP = j.id
        
        createinstance = ec2.create_instances(
           BlockDeviceMappings=[
              {
                  'DeviceName': '/dev/xvdh',
                  'VirtualName': 'ephemeral',
                  'Ebs': {
 #                     'Encrypted': True,
                      'DeleteOnTermination': False,
 #                    'KmsKeyId': 'string',
                      'SnapshotId': SNAP,
                      'VolumeSize': int(EBS),
                      'VolumeType': 'gp2'
                  },
             },
           ],
           ImageId=IMAGE,
           InstanceType=I_TYPE,
           KeyName= 'localkeypairnonprod',
           MaxCount=1,
           MinCount=1,
           SubnetId="subnet-033274069137eafae",
           UserData=user_data_script,
           
           TagSpecifications=[
              {
               'ResourceType': 'instance',
               'Tags': [
                    {
                       'Key': 'Name',
                       'Value': INSTANCE_NAME
                    },
                   ]
             },
           ],
           SecurityGroupIds=['sg-0a00f1371e5e23fc8'
           ],
     
        )
    
    for instance in createinstance:
        print('Please wait while instance is being launched...')
        while instance.state['Name'] not in ('running','stopped'):
            print("Please wait...")
            time.sleep(5)
            instance.load()
        print('\nInstance is ready to use. Login using public dns : ',instance.public_dns_name)
    

def terminate(RI_NAME,S_NEW_NAME=None):
    client = boto3.client('ec2')
    instance_vol = []
    RI_ID = None
    instance = [i for i in ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [RI_NAME]}, {'Name': 'instance-state-name', 'Values':['running']}])]
    for i in instance:
        RI_ID = i.id
        print(RI_ID)
    if RI_ID != None:
        print('\nWe are terminating...', RI_NAME)
    else:
        print("\nSeems you are trying to remove instance with don't exist")
        sys.exit(1)


    try:
        instance = ec2.Instance(RI_ID)
        for device in instance.block_device_mappings:
            if (device.get('DeviceName')) == '/dev/xvdh':
                volume = device.get('Ebs')
                instance_vol.append(volume.get('VolumeId'))
            

        response = client.terminate_instances(
            InstanceIds=[
                  RI_ID,
             ],
             DryRun=False
            )
        wait_time(RI_NAME)
        if(S_NEW_NAME == None):
            for vm in instance_vol:
                volume = ec2.Volume(vm)
                response = volume.delete()
            print("\nInstance terminated and volume deleted")
        else:
            for vm in instance_vol:
                try:
                    snapshot = ec2.create_snapshot(VolumeId=vm, Description="Snapshot from instance")
                    snapshot = ec2.Snapshot(snapshot.id)
                    tag = snapshot.create_tags(
                        Tags=[
                            {'Key': 'Name', 'Value': S_NEW_NAME },
                            ]
                          )
                    print("Creating snapshot")
                    while snapshot.state != 'completed':
                        print ("Snapshot under creation")
                        time.sleep(10)
                        snapshot.load()
                    else:
                        print("\nPlease save this snapshot name.Use it in next instance creation: ", S_NEW_NAME)
                        volume = ec2.Volume(vm)
                        response = volume.delete()
                        print("\nRespective Volume deleted")
                except:
                    raise          
    except:
           sys.exit(1)

def wait_time(RI_NAME):
    instance = [i for i in ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [RI_NAME]}])]
    for something in instance:
        print("Please wait while instance is being terminated...")
        while something.state['Name'] not in ('terminated'):
            print("Please wait...")
            time.sleep(5)
            something.load()
        print('\nInstance is terminated.')



if __name__ == '__main__':
    arguments = docopt(__doc__, version='launch 1.0')
    main(arguments)








