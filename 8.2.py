
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
		if len(words) == 0 : continue
		if words[0] != 'From' : continue
		print(words[2])
except:
	print('File is void of data')
	quit()

	#how do I detect if the file is truly empty and has no lines?