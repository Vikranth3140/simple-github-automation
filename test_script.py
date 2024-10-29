# test_script.py
from src.simple_github_automation.issue_management import create_issue, update_issue, close_issue

# Replace this with a test repo in the "username/repo" format
test_repo = "Vikranth3140/GitHub-Automation-Tools"

# 1. Test creating an issue
new_issue = create_issue(test_repo, "Test Issue", "This is a test issue created via the API.")
print("Create Issue Response:", new_issue)

# Extract issue number for further tests
issue_number = new_issue.get("number")
if issue_number:
    # 2. Test updating the issue
    updated_issue = update_issue(test_repo, issue_number, title="Updated Test Issue", body="Updated issue body.")
    print("Update Issue Response:", updated_issue)

    # 3. Test closing the issue
    closed_issue = close_issue(test_repo, issue_number)
    print("Close Issue Response:", closed_issue)
else:
    print("Failed to create an issue; skipping update and close tests.")
