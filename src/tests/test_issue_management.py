# test_issue_management.py
from github_automation.issue_management import create_issue

def test_create_issue():
    print("Running test_create_issue...")  # Add this line
    repo_name = "Vikranth3140/GitHub-Automation-Tools"
    title = "Test Issue"
    body = "This is a test issue body."

    response = create_issue(repo_name, title, body)
    assert response.get("title") == title
    assert response.get("body") == body
