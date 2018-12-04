
#!/bin/bash
##############
#Description: This script will create public key and private key for local user in a EC2 instance
#Author: Bhanupraaksh Suravarapu#
################################



##read -p "Enter keypair name for user : " key_pair_name

[ $# -eq 0 ] && { echo "Usage: create_user_keypair.sh <Keypair_name> $1"; exit 1; }


ssh-keygen -b 1024 -N "" -f  $1 -t dsa

cat $1 > $1'_privatekey.pem'
cat $1'.pub' > $1'_publickey'
rm $1 $1.'pub'

echo -e "\n Public key and privatekey with name $1 are saved in your current directory"




