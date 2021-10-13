import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/ym168")

donor  = requests.get(server_name + "get_blood_type/M8")
recipient  = requests.get(server_name + "get_blood_type/M5")

print(donor.text)
print(recipient.text)

check = (recipient.text == ("AB-" or "AB+"))
print(check)

request_json = {"Name": "ym168", "Match": "No"}
r = requests.post(server_name + "match_check", json=request_json)
print(r.text)