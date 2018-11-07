# Data Science

Data Science workflow tools and documentation.

**WARNING:** Do NOT put health care data in this or any other GitHub
repository.

## Using GitHub

For the unfamiliar, we can use GitHub's helpful [**Issues**](https://guides.github.com/features/issues/)
feature to track
our work and help our future selves and those selves that come after understand
our thought processes (this can greatly increase efficiency).

Austin suggests we simply ask questions **HERE** rather than through other
channels if there is any chance others will have the same question (very
common) by raising an Issue. In addition, Austin suggests we track  development
by raising and responding to issues. This provides a natural way to look back
for greater understanding, and may  help those that follow you (including
yourself), so you don't have to do the same thing twice nor spend time
explaining to somebody something they could be reading.

## Data Science Workflow using AWS

**Proper organization makes hard things easier.**

1. Construct AMI that has all necessary libraries to do Data Science on EC2
instance. This AMI must have internet access. Use this to spin up EC2
instances for working with medical data (no internet access).
2. Develop and experiment on EC2 instance with big data on a Jupyter notebook.
3. If written code is not a one-off, show proof of effectiveness by saving
notebook to GitHub `notebooks` repo (NO HEALTHCARE DATA, ONLY RESULTS!),
**and** pull the code into appropriate GitHub-backed library.
4. Make the push close an appropriately-raised issue that also refers to the
notebook for records.
5. Rinse and repeat.
