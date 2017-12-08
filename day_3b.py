target = 18
def create_layer(x):
	if x == 1:
		return [[1] for i in range(4)]
	else:
		return [[0 for j in range(x - 1)] for i in range(4)]

def next_index(arr, current_index):
	if current_index == len(arr) - 1:
		return 0  
	else:
		return current_index

def add_to_next_layer_incident_positions(side, number_index, num):
	side[number_index - 1] += num
	side[number_index] += num
	side[number_index + 1] += num

def add_to_last_two_of_list(ls, num):
	ls[len(ls) - 1] += num
	ls[len(ls) - 2] += num

def add_to_next_index(ls, i, num):
	ls[next_index(ls, i)] += num

def first_val_larger_helper(target_value, current_layer, next_layer, next_layer_size):
	for side_index, side in enumerate(current_layer):
		for number_index, num in enumerate(side):
			print(num)
			add_to_next_layer_incident_positions(next_layer[side_index], number_index, num)	
			if num >= target_value:
				return num
			elif number_index == 0:
				add_to_last_two_of_list(current_layer[side_index - 1], num)
				add_to_next_index(current_layer[side_index], number_index, num)
			elif number_index == len(side) - 2:
				add_to_next_index(current_layer[side_index], number_index, num)
				current_layer[next_index(current_layer, side_index)][0] += num
			elif number_index == len(side) - 1:
				next_layer[next_index(current_layer, side_index)][0] += num
				next_layer[next_index(current_layer, side_index)][1] += num
				current_layer[next_index(current_layer, side_index)][0] += num
			else:
				current_layer[side_index][next_index(side, number_index)] += num
	print("size", next_layer_size, "failed")
	return first_val_larger_helper(target_value, next_layer, create_layer(next_layer_size + 2), next_layer_size + 2)

def first_val_larger(target_value):
	first_layer = create_layer(1)
	second_layer = create_layer(3)
	return first_val_larger_helper(target_value, first_layer, second_layer, 3)

print(first_val_larger(target))

