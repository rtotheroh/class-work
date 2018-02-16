
x = input('Enter a file name:')

try:
	handle = open(x)
except:
	print('File', x, 'cannot be accessed') 
	exit()

wordsd = dict()
for line in handle:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		d1, d2, d3 = words[5].split(':')
		if d1 not in wordsd:
			wordsd[d1] = 1
		else:
			wordsd[d1] += 1

sortlist = list()
for valu, key in wordsd.items():
	sortlist.append( (valu, key) )
sortlist.sort()

for key, valu in sortlist :
		print(key, valu)

