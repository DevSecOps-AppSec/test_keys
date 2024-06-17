import csv
from github import Github

# Function to read CSV file and return data
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to add a workflow file to a GitHub repository
def add_workflow_to_repo(repo, default_branch):
    workflow_content = """
name: Gitleaks - Scanning Secrets in PR
on:
  push:
    branches:
      - 'track/dev'
      - 'track/test'
      - 'track/prod'
      - 'main'
      - 'master'
  pull_request:
    types:
      - synchronize
      - opened
    branches:
      - 'track/dev'
      - 'track/prod'
      - 'main'
      - 'master'
jobs:
  scan:
    name: gitleaks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.PAT_TOKEN }}
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}
""".format(default_branch, default_branch)

    try:
        repo.create_file(".github/workflows/gitleaks.yml", "Adding CI workflow", workflow_content, branch=default_branch)
        print(f"Workflow file added to {repo.full_name} successfully.")
    except Exception as e:
        print(f"Failed to add workflow file to {repo.full_name}. Error: {e}")

# GitHub credentials and organization name
github_token = 'PAT_TOKEN'
organization_name = 'ORG_NAME'

# Read repository information and default branch names from CSV
csv_file = 'data.csv'
repos_info = read_csv(csv_file)

# Connect to GitHub
g = Github(github_token)

# Get organization
org = g.get_organization(organization_name)

# Iterate over repositories and add workflow file
for repo_info in repos_info:
    repo_name = repo_info['Repository']
    default_branch = repo_info['DefaultBranch']

    # Get repository
    repo = org.get_repo(repo_name)

    # Add workflow file
    add_workflow_to_repo(repo, default_branch)
