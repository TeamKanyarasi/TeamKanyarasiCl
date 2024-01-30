# Task 1 : Jenkins CI CD pipeline for flask application
Automation of Python web app testing and deployment using Jenkins.
## Overview
This Jenkins pipeline automates the build, test, and deployment of a Flask application. It fetches the application code from a GitHub repository, installs dependencies, runs unit tests, and deploys to a staging environment.
## Prerequisites
Create an EC2 instance and install Jenkins server.
## Pipeline Stages
The pipeline includes these stages:

1. **Checkout:** Retrieves the application code from the GitHub repository.
2. **Build:** Installs application dependencies using `pip`.
3. **Test:** Runs unit tests for the application with `pytest`.
4. **Deploy:** Deploys the application to a staging environment if tests pass.
## Jenkinsfile Configuration

The Jenkinsfile defines pipeline stages and steps:

- `agent any`: Allows the pipeline to run on any available Jenkins agent.
- `git`: Fetches application code from GitHub repository using `git-cred` credentials.
- `pip install`: Installs dependencies from `requirements.txt`.
- `pytest`: Runs unit tests using the `pytest` framework.

[Jenkinsfile](https://github.com/TeamKanyarasi/TeamKanyarasiCl/blob/main/Jenkinsfile)

## Overall Workflow

1. Checkout code from GitHub repository.
2. Install dependencies using pip.
3. Run unit tests with pytest.
4. Deploy application to staging.
5. Send email notification indicating build status.

# Task 2 : Create a complete CI-CD pipeline using bash, python and crontabs. 

## Step 1: Set Up a Simple HTML Project 
 - Create a simple HTML project and push it to a GitHub repository. 
## Step 2: Set Up an AWS EC2/Local Linux Instance with Nginx
 - Launch an EC2 instance with Linux based AMI with Nginx server installed on it.
## Step 3: Write a Python Script to Check for New Commits
 - Created a Python script `auto.py` to check for new commits using the GitHub API.
## Step 4: Set Up a Cron Job to Run the Python Script
 - Created a cron job to run the Python script at regular intervals.
## Step 5: Test the Setup 
 - Made a new commit to the GitHub repository and check that the changes are automatically deployed. 
