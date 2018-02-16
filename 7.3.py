filename = input('Enter a file name: ')
count = 0

try:
	file = open(filename)
except:
	if filename == 'na na boo boo':
		print('Not so fast. You know that is not right')
		quit()
	else:
		print('Error. File cannot be openned.') 
		quit()
for line in file:
	if line.startswith('Subject:'):
		count = count + 1

#ffile = file[24:64]	

print('There were '+str(count)+' lines in '+filename)