import os

GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_REPOSITORY_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REVIEWERS = os.getenv("INPUT_REVIEWERS")

GITHUB_API_URL = "https://api.github.com"
GITHUB_HEADERS = {"Accept": "application/vnd.github.v3+json"}

print(GITHUB_REPOSITORY)
print(GITHUB_REPOSITORY_OWNER)
print(GITHUB_TOKEN[:3])
print(REVIEWERS)
