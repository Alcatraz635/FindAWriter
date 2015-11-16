import sys
from collections import Counter

lines = filter(None, (line.rstrip() for line in open(sys.argv[1], 'r')))

for line in lines:
    decoded = ''
    encoded = line.strip().split('|')[0]
    keys = list(line.strip().split('|')[1].split(' '))
    keys.pop(0)
    for key in keys:
        decoded = decoded + (encoded[int((key))-1])
    print decoded
    


exit(0)