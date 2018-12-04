#!/bin/bash


#####Enter your account id####

aws ec2 describe-snapshots --query 'Snapshots[*].{ID:SnapshotId,Size:VolumeSize,Time:StartTime,description:Description,Name:Tags[?Key==`Name`]|[0].Value}' --owner self --output table
