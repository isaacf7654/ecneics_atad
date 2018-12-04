# EC2 Instance Rules

1. Home directory size is limited to 10GB.
2. DHP Software located at: `/vol/dhplab`. Permissions are rwx. For software updates, open this with a public access-enabled instance.
3. Save big data (e.g., pulled data from SQL database) to `/vol/bigdata`.

| Directory | Size          | Example Contents                  | Maintained by  |
| --------- | ------------- | --------------------------------- | -------------- |
| `/`       | 10GB          | home directory, Installation      | sysadmin       |
| `/vol`    | user-selected | data science software, python env | data wranglers |
