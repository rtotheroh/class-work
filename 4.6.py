
def computepay(hours, rate):
	if hours <= 40:
		pay = hours * rate
	else: 
		pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
	return pay


try: 
	hours = float(input('Enter hours worked: '))
	rate = float(input('Pay rate without $: '))
	pay = computepay(hours, rate)
	print(pay)
except: 
	print('Error, please enter numeric input')
