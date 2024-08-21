from github import Github
import os
import json
import dotenv

# Load environment variables from .env file (if needed)
# dotenv.load_dotenv()

# Get your GitHub token from environment variables
token = os.getenv('GITHUB_TOKEN')

# Create a PyGithub object with authentication
g = Github(token)

username = 'mikaelaarzaga'
user = g.get_user(username)

# Initialize an empty list to store repository data
repo_data = []

# Fetch repositories
for repo in user.get_repos():
    repo_info = {
        'name': repo.name,
        'description': repo.description,
        'url': repo.html_url,
        'created_at': repo.created_at.isoformat(),
    }
    repo_data.append(repo_info)

    # Get the latest tag (if available)
    try:
        latest_tag = repo.get_tags()[0].name
        repo_info['latest_tag'] = latest_tag
    except IndexError:
        repo_info['latest_tag'] = "No tags found"

# Save data to a JSON file
with open('github_data.json', 'w') as json_file:
    json.dump(repo_data, json_file, indent=4)

# Convert data to AsciiDoc
asciidoc_content = ""
for repo in repo_data:
    asciidoc_content += f"== {repo['name']}\n\n"
    asciidoc_content += f"Description: {repo['description']}\n"
    asciidoc_content += f"URL: {repo['url']}\n"
    asciidoc_content += f"Created At: {repo['created_at']}\n"
    asciidoc_content += f"Latest Tag: {repo['latest_tag']}\n\n"

# Save to an AsciiDoc file (e.g., 'repos.adoc')
with open('repos.adoc', 'w') as adoc_file:
    adoc_file.write(asciidoc_content)

print("Data saved to github_data.json and converted to repos.adoc")
