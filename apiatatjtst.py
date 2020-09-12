ip = https://minecraftpocket-servers.com/api/?object=servers&element=voters&key=nzj3FwMNvH1eHqmhNrUPXTEEoMIYhMej&month=current

response = requests.get(ip)
json_response = response.json()
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
onpl = json_response['players']['online']

print(onpl)