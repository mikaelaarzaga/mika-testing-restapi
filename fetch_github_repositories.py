import requests
import os
import dotenv 

token = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token{token}'}

username = 'mikaelaarzaga'
url = f'https://api.github.com/users/{username}/repos'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()

    for repo in repos:
        print(f"Repository Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"URL: {repo['html_url']}")
        print(f"Created At: {repo['created_at']}")
        print('-' * 40)
else:
    print(f"Faile to fetch repositories: {response.status_code}")








# # GitHub API base URL
# GITHUB_API_URL = "https://api.github.com"

# # Fetch repository details function
# def get_repo_details(owner, repo, token=None):
#     # Construct the API URL for the repository
#     url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"
    
#     # Set headers, including authentication token if provided
#     headers = {
#         "Accept": "application/vnd.github.v3+json"
#     }
    
#     if token:
#         headers["Authorization"] = f"token {token}"
    
#     # Make the request to GitHub API
#     response = requests.get(url, headers=headers)
    
#     # Check for successful request
#     if response.status_code == 200:
#         # Parse JSON response
#         return response.json()
#     else:
#         return {"error": f"Unable to fetch repository details. Status code: {response.status_code}"}

# # Example usage
# if __name__ == "__main__":
#     owner = "octocat"  # GitHub username
#     repo = "Hello-World"  # Repository name
#     token = "your_personal_access_token"  # Optional, use your GitHub token
    
#     repo_details = get_repo_details(owner, repo, token)
    
#     # Print repository details
#     print(repo_details)
