#!/usr/bin/env python3
''' 
	api-test.py
	Max Goldberg, 1 October 2018

	This program accesses the API of the National Highway Traffic Safety Administration (NHTSA).
	It can access the models of a car given a vehicle make, and it can access all of the vehicle makes.
	API link- https://vpic.nhtsa.dot.gov/api/
'''

import argparse
import json
import urllib.request

def get_all_makes():
	'''
	Returns all of the makes in the database. The makes are returned as a list of strings.
	'''
	url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json'
	data_from_server = urllib.request.urlopen(url).read()
	string_from_server = data_from_server.decode('utf-8')
	make_list = json.loads(string_from_server)
	result_list = []
	for make in make_list['Results']:
		result_list.append(make['Make_Name'])
	return result_list

def get_models(make):
	'''
	Returns a list of models given the input string make.
	'''
	base_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{0}?format=json'
	url = base_url.format(make)
	data_from_server = urllib.request.urlopen(url).read()
	string_from_server = data_from_server.decode('utf-8')
	model_list = json.loads(string_from_server)
	result_list = []
	for model in model_list['Results']:
		result_list.append(model['Model_Name'])
	return result_list


def main(args):
	if args.action == 'models_from_make':
		if (args.make == None):
			print("Must specify -make argument")
			return
		make_list = get_models(args.make)
		for make in make_list:
			print(make)
	elif args.action == 'all_makes':
		makes_list = get_all_makes()
		for makes in makes_list:
			print(makes)

if __name__ == '__main__':
	print('''
This will print all makes:\n	python3 api-test.py all_makes
This will print all subaru models: \n	python3 api-test.py models_from_make -make \"subaru\"\n''')

	parser = argparse.ArgumentParser(description='Get Vehicle info from the NHTSA Vehicle API')

	parser.add_argument('action',
                        metavar='action',
                        help='m',
                        choices=['models_from_make', 'all_makes'])

	# Added an optional argument. (It is required when using "models_from_make", but it'll tell the user)
	parser.add_argument('-make',
			metavar='-make',
			help='which make to learn about- \'[return] will see all models')

	args = parser.parse_args()
	main(args)
