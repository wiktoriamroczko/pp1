import json

computer = {
    "brand" : "HP",
    "used" : False,
    "Memory card reader" : ['SD', 'SDHC', 'SDXC'],
    "year" : 2019,
    "parameters" : {
        "color" : "black",
        "type" : "laptop",
        "guarantee" : "2 years"
        }
    }

with open ('komputer.json', 'w') as file:
    json.dump(computer,file,indent=4)