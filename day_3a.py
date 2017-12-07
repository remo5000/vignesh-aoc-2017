target = 312051
k = 1
# TODO: replace with mad cow + binary search
while k ** 2 < target:
	k += 2
nearest_to_one = k ** 2 - ((k - 1) // 2)
distance_to_one = (k - 1) // 2
while abs(nearest_to_one - target) > ((k - 1) // 2):
	nearest_to_one -= (k - 1)
distance_to_nearest_number = abs(nearest_to_one - target)
distance_to_one += distance_to_nearest_number
print(distance_to_one)

