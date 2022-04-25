import requests
import json
url = "https://backend.credenz.in/api/check_user/"
myobj = {
    "username":"karan09",
    "password":"Credenz@123",
    "event":"WebWeaver"
}
# try:
userObj = requests.post(url, json = myobj)
# userObj = json.loads(userObj.text)

print(userObj)