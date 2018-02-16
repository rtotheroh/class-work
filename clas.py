def percentage(points_i_got, total_points):
	perc = points_i_got / total_points
	return perc

# how many points did you get?
# how many total?

x = 0
class_total = 0
class_points = 0
while(x < 3):
	total = float(input("how many points was the paper worth? "))
	points = float(input("how many points did you get? "))

	my_percentage = percentage(points, total)
	print(my_percentage)

	class_total = class_total + total
	class_points = class_points + points
	x += 1

print("My percentage of the class is:")
print(percentage(class_points, class_total))