#this is exercises 6


import yaml
import json


yaml_file = 'my_test1.yml'
json_file = 'my_test1.json'

my_dict = {

	'hostname': 'routerabc',
	'ntp': '10.1.1.1',
	'domain_name': 'gio.com'
	}

my_list = [
	'testing router 1',
	'testing router 2',
	my_dict,
	]


with open("my_test1.json", "w") as f:
	json.dump(my_list, f)


with open("my_test1.ymal", "w") as f:
    yaml.dump(my_list, f)



