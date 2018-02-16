
x = 'Data/INFX_511_Student_Data_Files/mbox-short.txt'
handle = open(x)
wordsd = dict()

for line in handle:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		start = words[1].find('@')
		domain = words[1][start+1:]
		if domain not in wordsd:
			wordsd[domain] = 1
		else:
			wordsd[domain] += 1

print(wordsd)

