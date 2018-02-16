
def count(word, q):
	number = 0
	for letter in word:
		if q == letter:
			number = number + 1
	return number

word = input('Enter a word: ')
letter = input('Enter the letter to be counted: ')
result = count(word, letter)
print(result)