file = input('Enter a file name: ')

handle = open(file)
for line in handle:
	stripline = line.rstrip()
	print(stripline.upper())
