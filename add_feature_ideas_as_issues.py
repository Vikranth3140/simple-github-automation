# add_feature_ideas_as_issues.py
from src.simple_github_automation.issue_management import create_issue

# Replace with your GitHub repository
repo_name = "Vikranth3140/simple-github-automation"

# List of feature ideas to add as issues
feature_ideas = [
    {
        "title": "Support for Custom Templates",
        "body": "Allow users to define custom issue and PR templates for more consistent formatting."
    },
    {
        "title": "Enhanced Reporting for Repository Insights",
        "body": "Add reporting capabilities, such as exporting contributor stats and issue summaries to CSV or PDF."
    },
    {
        "title": "Notifications Integration",
        "body": "Integrate with Slack or email to notify users about new issues, PRs, or other events."
    },
    {
        "title": "Advanced Labeling with NLP",
        "body": "Use natural language processing (NLP) to automatically label issues based on their content."
    },
    {
        "title": "Scheduled Tasks for Repository Maintenance",
        "body": "Allow users to schedule automated tasks like closing stale issues, reminding contributors, and more."
    }
]

# Loop through each feature idea and create an issue for it
for feature in feature_ideas:
    response = create_issue(repo_name, feature["title"], feature["body"])
if "html_url" in response:
    print(f"Issue created: {response['html_url']}")
else:
    print(f"Error: {response.get('error', 'Unknown error')}")
