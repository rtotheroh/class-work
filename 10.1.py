
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
		if words[1] not in wordsd:
			wordsd[words[1]] = 1
		else:
			wordsd[words[1]] += 1
sortlist = list()
for key, valu in wordsd.items():
	sortlist.append( (valu, key) )
sortlist.sort(reverse=True)

for key, valu in sortlist[:3] :
		print(key, valu)

