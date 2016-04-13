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


with open("my_test1.json") as f:
	json_list = json.load(f)


with open("my_test1.ymal" as f:
    yaml_list = yaml.load(f)
