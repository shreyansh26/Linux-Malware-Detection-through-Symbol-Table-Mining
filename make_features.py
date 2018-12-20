import pickle
from collections import Counter

file = open("benign.pickle", 'r')
benign_dict = pickle.load(file)
file.close()

file = open("malware.pickle", 'r')
malware_dict = pickle.load(file)
file.close()

malware_cnt = Counter(malware_dict)
benign_cnt = Counter(benign_dict)
final_cnt = malware_cnt + benign_cnt
# malware_dict.update(benign_dict)

for key, value in reversed(sorted(final_cnt.iteritems(), key=lambda (k,v): (v,k))):
    print "%s: %s" % (key, value)