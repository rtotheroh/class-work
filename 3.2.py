
try: 
	hours = float(input('Enter hours worked: '))
	rate = float(input('Pay rate without $: '))
	if hours <= 40:
		pay = hours * rate
	else: 
		pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
	print(pay)
except: 
	print('Error, please enter numeric input')
