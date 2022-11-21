import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = getpass('Paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {}

headers = {
	'Authorization': 'Bearer ' + TOKEN,
	'Content-Type': 'application/json'
	}
	
getRooms = BASEURL + room

response = requests.post(getRooms, headers=headers, data=body)

responseJSON = response.json()

pprint(responseJSON)
