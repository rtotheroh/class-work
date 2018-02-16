
def computegrade(grade):
	if grade >= 0.9 and grade <= 1.0:
		return('A')
	elif grade >= 0.8 and grade < 0.9:
		return('B')
	elif grade >= 0.7 and grade < 0.8:
		return('C')
	elif grade >= 0.6 and grade < 0.7:
		return('D')
	elif grade < 0.6 and grade > 0:
		return('F')
	
invalid_statement = 'Bad score'

try: 
	grade = float(input('Enter score between 0.0 and 1.0: '))
	if grade <= 1.0 and grade >= 0:
		letter_grade = computegrade(grade)
		print(letter_grade)
	else: 
		print(invalid_statement)
except: 
	print(invalid_statement)

