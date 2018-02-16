
x = input('Enter a file name:')

try:
	handle = open(x)
except:
	print('File', x, 'cannot be accessed') 
	exit()

wordsd = dict()
for line in handle:
	line = line.lower()
	for l in line:
		if l not in 'abcdefghijklmnopqrstuvwxyz': continue
		if l not in wordsd:
			wordsd[l] = 1
		else:
			wordsd[l] += 1

sortlist = list()
for key, valu in wordsd.items():
	sortlist.append( (valu, key) )
sortlist.sort(reverse = True)

for key, valu in sortlist :
		print(key, valu)

