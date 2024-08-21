from github import Github
import os
import json
import dotenv

# Load environment variables from .env file (if needed)
#dotenv.load_dotenv()

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

# Load existing data from github_data.json (if it exists)
existing_data = []
if os.path.exists('github_data.json'):
    with open('github_data.json', 'r') as existing_file:
        existing_data = json.load(existing_file)

# Merge new data with existing data
all_data = existing_data + repo_data

# Save updated data to github_data.json
with open('github_data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)

# Convert data to AsciiDoc table format
asciidoc_content = "== Repository Details\n\n"
asciidoc_content += "|===\n"
asciidoc_content += "| Repository Name | Description | URL | Created At | Latest Tag\n"

for repo in all_data:
    asciidoc_content += f"| {repo['name']} | {repo['description']} | link:{repo['url']} | {repo['created_at']} | {repo['latest_tag']}\n"

asciidoc_content += "|===\n"

# Save to an AsciiDoc file (e.g., 'repos.adoc')
with open('repos.adoc', 'w') as adoc_file:
    adoc_file.write(asciidoc_content)

print("Data updated and saved to github_data.json and converted to repos.adoc")
