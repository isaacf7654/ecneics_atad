# Data Science

Data Science workflow tools and documentation.

**WARNING:** Do NOT put health care data in this or any other GitHub
repository.

## Using GitHub

For the unfamiliar, we can use GitHub's helpful [**Issues**](https://guides.github.com/features/issues/)
feature to track
our work and help our future selves and those selves that come after understand
our thought processes (this can greatly increase efficiency).

Austin suggests we simply ask questions **HERE** (with Issues) rather than through other
channels if there is any chance others will have the same question (very
common) by raising an Issue. In addition, Austin suggests we track  development
by raising and responding to issues. This provides a natural way to look back
for greater understanding, and may  help those that follow you (including
yourself), so you don't have to do the same thing twice nor spend time
explaining to somebody something they could be reading.

## Data Science Workflow using AWS

See AWS EC2 Walkthrough Word document [here](https://launchpointcorporation-my.sharepoint.com/:w:/g/personal/aprivett_discoveryhealthpartners_com/EX0oajtn7hlGr1dBPc25V-QB3zYM6DeV2hQXwdgj2XdRxQ?e=TnLsiU).

**Proper organization makes hard things easier.**

1. Construct AMI that has all necessary libraries to do Data Science on EC2
instance. This AMI must have internet access. Use this to spin up EC2
instances for working with medical data (no internet access). Any changes you
want to save after that point must go over SSH (either use SCP or copy/paste
across editor).
2. Develop and experiment on EC2 instance with big data on a Jupyter notebook.
3. If written code is not a one-off, show proof of effectiveness by saving
notebook to GitHub `notebooks` repo (NO HEALTHCARE DATA, ONLY RESULTS!),
**and** pull the code into appropriate GitHub-backed library.
4. Make the push close an appropriately-raised issue that also refers to the
notebook for records.
5. Rinse and repeat.

## Engineered Features

See [this spreadsheet](https://launchpointcorporation-my.sharepoint.com/:x:/g/personal/aprivett_discoveryhealthpartners_com/EaaAFunfBMZNh6Wyx5AI6PcB5_wDyeEuFUX5QQevik3nCA?e=poLise) 
for a list of useful engineered features.

## Installing new packages on an EC2 instance (pip and conda)

1. Ask Bhanu to open the Public Access.
1. Use https://github.com/dhplabs/data-science/blob/master/ec2/launch_and_terminate_instance_publicAccess.py and follow the create instance instructions.
2. Then, install everything you need using pip, etc.
3. Ask Bhanu for the next step. Tell him you're done and the public access can be closed.

(In the future, we'll have a firewall and won't have to manually open/close the channel.)

## Supported EC2 instance types

- [x] t2
- [ ] t3

# EC2 Instance Rules

1. Home directory size is limited to 10GB.
2. DHP Software located at: `/vol/dhplab`. Permissions are rwx. For software updates, open this with a public access-enabled instance.
3. Save big data (e.g., pulled data from SQL database) to `/vol/bigdata`.

| Directory | Size          | Example Contents                  | Maintained by  |
| --------- | ------------- | --------------------------------- | -------------- |
| `/`       | 10GB          | home directory, Installation      | sysadmin       |
| `/vol`    | user-selected | data science software, python env | data wranglers |

## Rotating Access Keys

1. Generate new keys as shown [here](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/).
2. Run `aws configure` CLI to update keys on the local machine.

