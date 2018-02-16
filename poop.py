def poopypants(toilets, time):
	poops = toilets * time
	return poops

minutes = float(input('How many minutes did you poop for?: '))
bathrooms = float(input('How many bathrooms did you stink up?: '))

total = poopypants(bathrooms, minutes)
print("I took " + str(total) + " dumps today!")