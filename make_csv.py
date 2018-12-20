import pickle
import csv
import os
import re
from subprocess import call

headers = ['name']

with open('features_less.txt', 'r') as f:
	for l in f:
		a = l.split(': ')[0]
		headers.append(a)

headers.append('labels')
if not os.path.exists('./check.csv'):
	with open("check.csv", "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(headers)

PATH = './elf'
s = re.compile('<.+>')
symbols = re.compile('"\w+"')

for i in os.listdir(PATH):
	calls = dict()
	row = [0]*len(headers)
	row[0] = i
	row[len(headers)-1] = '?'
	file = os.path.join(PATH, i)
	if os.path.isfile(file):
		print file
		call('objdump -M intel -D ' + file[2:] + ' > hello.txt', shell=True)
		with open('hello.txt', 'r') as f:
			for l in f:
				if 'call   ' in l.strip():
					ind = l.strip().index('call   ')
					new_str = l.strip()[ind:]
					m = re.findall(s, new_str)
					if m:
						new_str = m[0]
					if (('Base' in new_str and 'Base+' not in new_str) or ('plt' in new_str)) and new_str in headers:
						if new_str not in calls.keys():
							calls[new_str] = 1;
						else:
							calls[new_str] += 1

		for i in calls.keys():
			row[headers.index(i)] = calls[i]

		with open("check.csv", "ab") as csv_file:
			writer = csv.writer(csv_file, delimiter=',')
			writer.writerow(row)
