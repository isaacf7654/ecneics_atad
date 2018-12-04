#!/bin/bash


#####Enter your account id####


aws ec2 describe-images --query 'Images[*].{ID:ImageId,OwnerID:OwnerId,Time:CreationDate,Status:State,Public:Public,Root_Device:RootDeviceType,AMIName:Tags[?Key==`Name`]|[0].Value}' --owners self --output table
