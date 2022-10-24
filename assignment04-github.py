import requests
import json
from github import Github
from config_week4 import config as cfg

# get the github key value from the config file
apikey = cfg["githubkey"]

g = Github(apikey)

# private repo reference
url = "https://api.github.com/repos/micheal-mcenery/week_4_assignment"

repo = g.get_repo("micheal-mcenery/week_4_assignment")

# get the download url of the file from the repository
fileInfo = repo.get_contents("week_4.txt")
urlOfFile = fileInfo.download_url

# get the data of the file
response = requests.get(urlOfFile)
# copy the contents of the file into a variable
contentOfFile = response.text

# replace all instances of Andrew with Micheal, and assign string to new variable
newContents = contentOfFile.replace("Andrew", "Micheal")

# update the file on the repository
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)