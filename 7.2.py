file = input('Enter a file name: ')

handle = open(file)
count = 0
result = 0.0

for line in handle:
	if line.startswith('X-DSPAM-Confidence:'):
		x = float(line[20:])
		result = result + x
		count = count + 1

print("Average spam confidence: ", result/count)


