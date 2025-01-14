# simple github automation

**simple github automation** is a Python package that allows you to automate common GitHub tasks, such as managing issues, automating pull requests, retrieving repository insights, and adding labels based on keywords or user mentions.

View it at [PyPI](https://pypi.org/project/simple-github-automation/)

## Features

- **Issue Management**: Create, update, and close issues programmatically.
- **Pull Request Automation**: Automate actions like creating pull requests, adding labels, and posting comments.
- **Repository Insights**: Fetch repository stats, list contributors, and get the count of open issues.
- **Automated Labeling**: Add predefined labels to issues or pull requests based on keywords or user mentions.

Yes, adding the directory structure is a great idea! It gives users a clear understanding of the project’s organization, especially if they want to explore or contribute to the codebase. Here’s an updated section for the **Directory Structure**:

## Installation

To install the package, use the following command:

```bash
pip install simple_github_automation
```

## Directory Structure

The project is organized as follows:

```plaintext
simple_github_automation/
├── src/
│   └── simple_github_automation/
│       ├── __init__.py                  # Initializes the package
│       ├── issue_management.py          # Issue management functions (create, update, close issues)
│       ├── pull_request_actions.py      # Pull request automation functions (create PR, add label, comment)
│       ├── repo_insights.py             # Repository insights functions (stats, contributors, open issues)
│       ├── automated_labels.py          # Automated labeling functions based on keywords and mentions
│       └── config.py                    # Configuration for API token
├── tests/
│   ├── test_issue_management.py         # Unit tests for issue management functions
│   ├── test_pull_request_actions.py     # Unit tests for pull request automation functions
│   ├── test_repo_insights.py            # Unit tests for repository insights functions
│   └── test_automated_labels.py         # Unit tests for automated labeling functions
├── setup.py                             # Installation file for the package
├── pyproject.toml                       # Build configuration
├── README.md                            # Documentation file
├── LICENSE                              # License file
└── .gitignore                           # File specifying ignored files and folders
```

Each section of the `src/simple_github_automation/` folder corresponds to specific functionality, with tests in the `tests/` folder.

## Configuration

To use this package, you need a GitHub Personal Access Token (PAT) with the necessary permissions.

1. **Generate a GitHub Token**:
   - Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
   - Create a new token with `repo` scope (for private and public repositories).
   
2. **Set Up Environment Variable**:
   - Set the token as an environment variable named `GITHUB_TOKEN`.
   
   **Example for Windows (PowerShell)**:
   ```powershell
   $env:GITHUB_TOKEN="your_github_token_here"
   ```

## Usage Examples

### 1. Issue Management

#### Creating an Issue
```python
from simple_github_automation.issue_management import create_issue

repo_name = "your_username/repo_name"
response = create_issue(repo_name, "New Issue Title", "Issue description here")
print(response)
```

#### Updating an Issue
```python
from simple_github_automation.issue_management import update_issue

issue_number = 1
response = update_issue(repo_name, issue_number, title="Updated Title", body="Updated description")
print(response)
```

#### Closing an Issue
```python
from simple_github_automation.issue_management import close_issue

response = close_issue(repo_name, issue_number)
print(response)
```

### 2. Pull Request Automation

#### Creating a Pull Request
```python
from simple_github_automation.pull_request_actions import create_pull_request

response = create_pull_request(repo_name, "feature-branch", "main", "New PR Title", "Description of PR")
print(response)
```

#### Adding Labels to a PR
```python
from simple_github_automation.pull_request_actions import add_label_to_pr

response = add_label_to_pr(repo_name, pr_number, ["bug", "enhancement"])
print(response)
```

#### Posting a Comment on a PR
```python
from simple_github_automation.pull_request_actions import post_comment_to_pr

response = post_comment_to_pr(repo_name, pr_number, "This is a comment on the PR.")
print(response)
```

### 3. Repository Insights

#### Getting Repository Stats
```python
from simple_github_automation.repo_insights import get_repo_stats

response = get_repo_stats(repo_name)
print(response)
```

#### Listing Contributors
```python
from simple_github_automation.repo_insights import list_contributors

response = list_contributors(repo_name)
print(response)
```

#### Getting Open Issues Count
```python
from simple_github_automation.repo_insights import get_open_issues_count

response = get_open_issues_count(repo_name)
print(response)
```

### 4. Automated Labeling

#### Adding Labels Based on Keywords
```python
from simple_github_automation.automated_labels import add_labels_by_keywords

keyword_label_map = {
    "bug": "bug",
    "urgent": "priority"
}
content = "This is an urgent bug report."
response = add_labels_by_keywords(repo_name, issue_number, content, keyword_label_map)
print(response)
```

#### Adding Labels Based on Mentions
```python
from simple_github_automation.automated_labels import add_labels_by_mentions

mention_label_map = {
    "username": "assigned"
}
content = "Assigning this task to @username."
response = add_labels_by_mentions(repo_name, issue_number, content, mention_label_map)
print(response)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.