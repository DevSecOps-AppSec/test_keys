import requests
import base64
import urllib.parse

# GitHub API endpoint
github_api = "https://api.github.com/repos"

# GitHub token
token = "PAT_TOKEN"

# File containing repository names
repos_file = "non_archived_repos.txt"

# Read repository names from the file
with open(repos_file, 'r') as f:
    repos = f.read().splitlines()

# Iterate over each repository
for repo_name in repos:
    # Repository owner
    owner = "Capillary"
    
    # Repository name (read from the file)
    repo = repo_name

    # File path
    path = urllib.parse.quote(".github/workflows/gitleaks_secret_scan.yml")
    print(path)
    # Commit message
    commit_message = "Adding GitLeaks Workflow"

    # Content
    content = """
    name: Gitleaks - Scanning Secrets in PR
    on:
      push:
        branches:
          - 'main'
          - 'master'
      pull_request:
        types:
          - synchronize
          - opened
        branches:
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
              GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE}}
    """

    # Committer information
    committer_name = "Souradip Ghosh"
    committer_email = "Email ID"

    # Construct the API URL
    api_url = f"{github_api}/{owner}/{repo}/contents/{path}"

    # Encode content
    encoded_content = base64.b64encode(content.encode()).decode()

    # Data payload
    data = {
        "message": commit_message,
        "content": encoded_content
    }

    # Headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Make the request
    response = requests.put(api_url, headers=headers, json=data)

    # Check response
    if response.status_code == 201:
        print(f"File created successfully for repository: {repo}")
    else:
        print(f"Failed to create file for repository: {repo}. Status code: {response.status_code}")
        print(f"Response content: {response.content}")
