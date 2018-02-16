grade = float(input('Enter score: '))
if grade >= 0.9 and grade <= 1.0:
	print('A')
elif grade >= 0.8 and grade < 0.9:
	print('B')
elif grade >= 0.7 and grade < 0.8:
	print('C')
elif grade >= 0.6 and grade < 0.7:
	print('D')
elif grade < 0.6 and grade >= 0:
	print('F')
else:
	print("invalid.")