#!/bin/bash
# Updates by Austin Privett 9/27/18
# Give location to ssh to.

## script to list out all instances ##

aws ec2 describe-instances --query 'Reservations[*].Instances[*].{PublicDnsName:PublicDnsName,ID:InstanceId,InstanceType:InstanceType,InstanceState:State.Name,LaunchTime:LaunchTime,Name:Tags[?Key==`Name`]|[0].Value}' --output table
