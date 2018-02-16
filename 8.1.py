
handt = ['a', 'b', 'c', 'd', 'e']

def chop(handt):
	del handt[0]
	del handt[len(handt)-1]

chop(handt)
print(handt)

