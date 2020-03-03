import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('data.json', 'r') as file:
    data = json.load(file)

for elements in data:
    client_name = elements["client_name"]
    redirection = elements["needs_client_redirection"],
    user_name = elements["UserName"]

response = requests.get("http://wayf.cesi.fr/login?client_name=%s&needs_client_redirection=%s&UserName=%s" % (client_name, redirection, user_name), verify=False)

print(response.content)
