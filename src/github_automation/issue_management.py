# issue_management.py
import requests
from .config import GITHUB_TOKEN

def create_issue(repo_name, title, body):
    """
    Creates an issue in the specified GitHub repository.

    Args:
        repo_name (str): Format as 'username/repo'.
        title (str): Title of the issue.
        body (str): Description or body of the issue.

    Returns:
        dict: Response from GitHub API.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "title": title,
        "body": body,
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Issue created successfully!")
    else:
        print("Failed to create issue:", response.json())
    
    return response.json()
