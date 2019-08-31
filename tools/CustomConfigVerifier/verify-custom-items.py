'''
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import json
import argparse
import re
import sys
import os
from collections import defaultdict
from os import path
from os import walk

opt = argparse.ArgumentParser()
opt.add_argument('path', help='The path to the root custom item directory to verify.')
args = opt.parse_args()

if(not path.isdir(args.path)):
	print('Not a directory: ' + args.path)
	sys.exit(1)
	
regex_lowercase_alphanumeric = re.compile('^[a-z0-9]*$')
regex_not_whitespace = re.compile('.*\S.*')
errors = defaultdict(list)
mandatory_keys = ['ckey', 'character_name']
key_value_alphanumeric =  ['ckey']
key_value_no_whitespace = ['character_name', 'item_name', 'item_desc', 'item_path', 'item_icon_state']
key_value_array =         ['req_access', 'req_titles']
key_value_dictionary =    ['additional_data']

for root, dirs, files in os.walk(args.path):
	for file in files:
		if file.endswith('.json'):
			inputPath = os.path.join(root, file)
			try:
				inputFile = open(inputPath, 'r')
				inputJson = json.loads(inputFile.read())
				inputFile.close()
				for mandatory_key in mandatory_keys:
					if not mandatory_key in inputJson:
						errors[inputPath].append('Missing mandatory key: %s' % mandatory_key)
				found_keys = defaultdict(int)
				for key in inputJson:
					found_keys[key] = found_keys[key] + 1
					if found_keys[key] > 1:
						print("1 %s" % key)
						errors[inputPath].append('Duplicate key: %s' % key)
					elif key in key_value_alphanumeric:
						if not regex_lowercase_alphanumeric.match(inputJson[key]):
							errors[inputPath].append("Invalid format - expected lowercase alphanumeric string: %s" % str(inputJson[key]))
					elif key in key_value_no_whitespace:
						if not regex_not_whitespace.match(inputJson[key]):
							errors[inputPath].append("Invalid format - expected whitespace-free string: %s" % str(inputJson[key]))
					elif key in key_value_array:
						if not isinstance(inputJson[key], list):
							errors[inputPath].append("Invalid format - expected list: %s" % str(inputJson[key]))
					elif key in key_value_dictionary:
						if not isinstance(inputJson[key], dict):
							errors[inputPath].append("Invalid format - expected dictionary: %s" % str(inputJson[key]))
					else:
						errors[inputPath].append("Unknown key: %s" % key)
			except Exception as ex:
				template = "Exception of type {0}:\n{1!r}"
				errors[inputPath].append(template.format(type(ex).__name__, ex.args))

for file_path, error_list in errors.items():
	if len(error_list) == 1:
		print('%s: %s' % (file_path, error_list[0]))
	else:
		print(file_path)
		for error in error_list:
			print("\t%s" % error)

if len(errors) > 0:
	sys.exit(1)
