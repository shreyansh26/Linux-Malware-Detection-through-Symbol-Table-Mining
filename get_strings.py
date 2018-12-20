import re
from subprocess import call
import os
import pickle
# sort bash_calls.txt | uniq -c | awk '{printf "%s : %s\n", $1, $2}' | sort -nr > bash_calls_frequency.txt

PATH = './'
s = re.compile('<.+>')
symbols = re.compile('"\w+"')

calls = dict()
system_calls = set()
all_calls = list()

for i in os.listdir(PATH):
	file = os.path.join(PATH, i)
	if os.path.isfile(file) and os.access(file, os.X_OK):
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
					if ('Base' in new_str and 'Base+' not in new_str) or ('plt' in new_str):
						if new_str not in calls.keys():
							calls[new_str] = 1;
						else:
							calls[new_str] += 1

# for key, value in sorted(calls.iteritems(), key=lambda (k,v): (v,k)):
#     print "%s: %s" % (key, value)

# with open('benign.pickle', 'wb') as handle:
# 	pickle.dump(calls, handle)