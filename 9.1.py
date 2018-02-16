
x = 'Data/INFX_511_Student_Data_Files/words.txt'
handle = open(x)
wordsd = dict()

for line in handle:
	words = line.split()
	for word in words:
		if word not in wordsd:
			wordsd[word] = 1
		else:
			wordsd[word] += 1
print(wordsd)
