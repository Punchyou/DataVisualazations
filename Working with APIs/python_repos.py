import requests

# Make an API call and store the responce.
url = "https://api.github.com/search/repositories?q=language:python&sorted=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a var.
response_dict = r.json()
print("Total resos:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first respository.
repo_dict = repo_dicts[0]
print('\nKeys: ', len(repo_dict))
for key in sorted(repo_dict):
    print(key)
print("Name: ", repo_dict['name'])