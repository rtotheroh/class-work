
x = []

while True:
	line = input('Enter a number: ')
	if line == 'done':
		break
	try:
		number = float(line) 
	except:
		print('Invalid') 
		continue
	result = x.append(number)

print('Minimum: ', min(x), 'Maximum: ', max(x))

