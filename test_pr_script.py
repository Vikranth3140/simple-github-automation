# test_pr_script.py
from src.simple_github_automation.pull_request_actions import create_pull_request, add_label_to_pr, post_comment_to_pr

# Replace with your test repository and branches
repo_name = "Vikranth3140/GitHub-Automation-Tools"
head = "feature-branch"
base = "main"
title = "Test Pull Request"
body = "This is a test pull request created via the GitHub API."

# 1. Test creating a pull request
new_pr = create_pull_request(repo_name, head, base, title, body)
print("Create Pull Request Response:", new_pr)

# Extract PR number for further tests
pr_number = new_pr.get("number")
if pr_number:
    # 2. Test adding labels to the PR
    label_response = add_label_to_pr(repo_name, pr_number, ["bug", "enhancement"])
    print("Add Label to PR Response:", label_response)

    # 3. Test posting a comment to the PR
    comment_response = post_comment_to_pr(repo_name, pr_number, "This is a test comment.")
    print("Post Comment to PR Response:", comment_response)
else:
    print("Failed to create pull request; skipping label and comment tests.")
