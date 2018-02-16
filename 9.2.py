
x = 'Data/INFX_511_Student_Data_Files/mbox-short.txt'
handle = open(x)
wordsd = dict()

for line in handle:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		if words[2] not in wordsd:
			wordsd[words[2]] = 1
		else:
			wordsd[words[2]] += 1
print(wordsd)
