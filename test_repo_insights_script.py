# test_repo_insights_script.py
from src.github_automation.repo_insights import get_repo_stats, list_contributors, get_open_issues_count

# Replace with your test repository
repo_name = "Vikranth3140/GitHub-Automation-Tools"

# 1. Test getting repository statistics
repo_stats = get_repo_stats(repo_name)
print("Repository Stats:", repo_stats)

# 2. Test listing contributors
contributors = list_contributors(repo_name)
print("Contributors:", contributors)

# 3. Test getting open issues count
open_issues_count = get_open_issues_count(repo_name)
print("Open Issues Count:", open_issues_count)
