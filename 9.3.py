
x = 'Data/INFX_511_Student_Data_Files/mbox-short.txt'
handle = open(x)
wordsd = dict()

for line in handle:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		if words[1] not in wordsd:
			wordsd[words[1]] = 1
		else:
			wordsd[words[1]] += 1
print(wordsd)