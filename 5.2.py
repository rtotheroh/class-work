
largest = None
smallest = None

while True:
	line = input('Enter a number: ')
	try:
		number = float(line) 
		if largest == None or number > largest:
			largest = number
		if smallest == None or number < smallest:
			smallest = number
	except:
		if line == 'done':
			break		 
		else: 
			print('Invalid') 

print(largest, smallest)



