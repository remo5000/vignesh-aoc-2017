target = 312051
k = 1
# TODO: replace with mad cow + binary search
while k ** 2 < target:
	k += 2
max_dist_to_one = k - 1
min_dist_to_one = max_dist_to_one // 2
nearest_to_one = k ** 2 - min_dist_to_one
distance_to_one = min_dist_to_one
while abs(nearest_to_one - target) > min_dist_to_one:
	nearest_to_one -= max_dist_to_one
distance_to_nearest_number = abs(nearest_to_one - target)
distance_to_one += distance_to_nearest_number
print(distance_to_one)

