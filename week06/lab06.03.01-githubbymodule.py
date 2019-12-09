# week6 lab3 python packages
from github import Github
import requests


# github key
g = Github("fdcba01d190e2a816c7468a196f5ff4cca3c1b01")

# get all repositories from github for my user
#for repo in g.get_user().get_repos():
#  print(repo.name)

# get a clone url of the repository
repo = g.get_repo("jobur123/PrivateOne")
#print(repo.clone_url)

# get the download url of the file in the repos
fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

#Use the download_url to make a http request to the file can output the contents of the file (TEXT contents).
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

# Append the text more stuff to the readme
newContents = contentOfFile + "\nmore stuff \n"
#print(newContents)

# update github
gitHubResponse = repo.update_file(fileInfo.path, "updated by program", newContents, fileInfo.sha)
print(gitHubResponse)