
x = open('Data/INFX_511_Student_Data_Files/romeo.txt')
result = []

for line in x: 
	words = line.split()
	for word in words:
		if word in result: continue
		result.append(word)

result.sort()
print(result)


