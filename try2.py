from github import Github
import os
import dotenv

# Load environment variables from .env file (if needed)

# Get your GitHub token from environment variables
token = os.getenv('GITHUB_TOKEN')

# Create a PyGithub object with authentication
g = Github(token)

username = 'mikaelaarzaga'
user = g.get_user(username)

# Fetch repositories
for repo in user.get_repos():
    print(f"Repository Name: {repo.name}")
    print(f"Description: {repo.description}")
    print(f"URL: {repo.html_url}")
    print(f"Created At: {repo.created_at}")

    # Get the latest tag (if available)
    try:
        latest_tag = repo.get_tags()[0].name
        print(f"Latest Tag: {latest_tag}")
    except IndexError:
        print("No tags found for this repository.")

    print('-' * 40)