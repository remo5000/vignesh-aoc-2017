target = 12
k = 1
# TODO: replace with mad cow + binary search
while k**2 < target:
	k += 2
nearest_to_one = k**2 - ((k - 1) // 2)
print("nearest_to_one", nearest_to_one)
distance_to_one = (k - 1) // 2
print("distance_to_one", distance_to_one)
distance_to_nearest_number = 0
while nearest_to_one - target >= 0 and target != 1:
	distance_to_nearest_number = nearest_to_one - target
	print("distance_to_nearest_number", distance_to_nearest_number)
	nearest_to_one -= (k - 1)
	print("new nearest_to_one", nearest_to_one)
distance_to_one += distance_to_nearest_number

print(distance_to_one)

