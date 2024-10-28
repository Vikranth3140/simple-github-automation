# test_automated_labels_script.py
from src.github_automation.automated_labels import add_labels_by_keywords, add_labels_by_mentions

# Replace with your test repository and issue/PR number
repo_name = "Vikranth3140/GitHub-Automation-Tools"
issue_number = 1  # Example issue/PR number

# Test adding labels by keywords
keyword_label_map = {
    "bug": "bug",
    "enhancement": "enhancement",
    "urgent": "priority"
}
content = "This is an urgent bug report that needs fixing."
keyword_labels_response = add_labels_by_keywords(repo_name, issue_number, content, keyword_label_map)
print("Keyword Labels Response:", keyword_labels_response)

# Test adding labels by mentions
mention_label_map = {
    "Vikranth3140": "assigned",
    "username2": "reviewer"
}
mention_content = "Assigning this issue to @Vikranth3140 for review."
mention_labels_response = add_labels_by_mentions(repo_name, issue_number, mention_content, mention_label_map)
print("Mention Labels Response:", mention_labels_response)
