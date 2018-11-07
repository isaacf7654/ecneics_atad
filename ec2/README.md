Austin Privett
8/16/2018

# Short Version

1. Get new packages `pip install boto3 doctopt`
2. Run `bash create_user_keypair.sh`
3. Configure AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) with `aws configure`
 * You'll need a key pair (above link)
 * us-east-1
 * Output format: text/json/table
4. Trouble from end-of-line? dos2unix

# More Information

Read `AWS_EC2_Walkthrough.docx`.
