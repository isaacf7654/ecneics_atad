# Development Workflow

Congratulations! You're up and running on a scalable EC2 instance! Fun, right!?
This is great if you want to simply run your already-developed code.

But what if you have significant development to do? How can you use your
favorite powerful IDE and workflow?

## Objective

Fully-featured development capabilities on the EC2 instance.

## Constraints

1. We must use Windows laptops as a thin client.
2. We must only connect over SSH to the secure environment.
  - Potential solution: SSHFS (AP used previously successfully for HPC).
  - Unfortunately, I believe this would require either Mac or Linux client.
3. Implication:
