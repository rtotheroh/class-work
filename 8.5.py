
x = 'Data/INFX_511_Student_Data_Files/mbox-short.txt'

try:
	x = open(x)
except:
	print('This file was not found: ', x)
count = 0
try:
	for line in x:
		words = line.split()
		if not len(words) == 0 and words[0] == 'From' :
			print(words[1])
			count = count + 1
except:
	print('The file is empty')
	quit()
print('The file contains', count, 'lines with From as the first word in the line.')