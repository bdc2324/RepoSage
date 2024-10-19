from github import Github

# Replace 'your_personal_access_token' with your GitHub Personal Access Token
ACCESS_TOKEN = 'your_personal_access_token'
REPO_NAME = 'your_username/your_repo'  # Replace with your GitHub username and repository name

# Initialize GitHub object with your access token
g = Github(ACCESS_TOKEN)

# Get the repository object
repo = g.get_repo(REPO_NAME)

# Example 1: Get general repository information
print(f"Repository Name: {repo.name}")
print(f"Owner: {repo.owner.login}")
print(f"Description: {repo.description}")
print(f"Stars: {repo.stargazers_count}")
print(f"Forks: {repo.forks_count}")
print(f"Open Issues: {repo.open_issues_count}")

# Example 2: List all files in the repository
def list_files_in_repo(repo):
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            print(f"File: {file_content.path}")

list_files_in_repo(repo)

# Example 3: Get the content of a specific file
file_path = 'README.md'  # Replace with the path of the file you want to fetch
try:
    file_content = repo.get_contents(file_path)
    print(f"\nContent of {file_path}:\n{file_content.decoded_content.decode()}")
except Exception as e:
    print(f"Error: {e}")
