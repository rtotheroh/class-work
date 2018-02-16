
x = 'Data/INFX_511_Student_Data_Files/mbox-short.txt'
count = 0

try: 
	fhand = open(x)
except:
	print('No file exists for: ', x)
	quit()

try:
	for line in fhand: 
		words = line.split()
		if not len(words) == 0 and words[0] == 'From' : print(words[2])
except:
	print('File is void of data')
	quit()

