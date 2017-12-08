target = 18
def create_layer(x):
	if x == 1:
		return [[1] for i in range(4)]
	else:
		return [[0 for j in range(x - 1)] for i in range(4)]

# def add_to_next_layer_adjacent_positions(num, number_index, next_side):
# 	next_side[number_index - 1] += num
# 	next_side[number_index] += num
# 	next_side[number_index + 1] += num

def next_index(arr, current_index):
	if current_index == len(arr) - 1:
		return 0  
	else:
		return current_index


def first_val_larger_helper(target_value, current_layer, current_layer_size, next_layer):
	for side_index, side in enumerate(current_layer):
		for number_index, num in enumerate(side):
			next_layer[side_index][number_index - 1] += num
			next_layer[side_index][number_index] += num
			next_layer[side_index][number_index + 1] += num
			if num >= target_value:
				return num
			elif number_index == 0:
				current_layer[side_index - 1][len(side) - 1] += num
				current_layer[side_index - 1][len(side) - 2] += num
				current_layer[side_index][next_index(side, number_index)] += num
			elif number_index == len(side) - 2:
				current_layer[side_index][next_index(side, number_index)] += num
				current_layer[next_index(current_layer, side_index)][0] += num
			elif number_index == len(side) - 1:
				next_layer[next_index(current_layer, side_index)][0] += num
				next_layer[next_index(current_layer, side_index)][1] += num
				current_layer[next_index(current_layer, side_index)][0] += num
			else:
				current_layer[side_index][next_index(side, number_index)] += num
	return first_val_larger_helper(target_value, next_layer, current_layer_size + 4, create_layer(current_layer_size + 4))

def first_val_larger(target_value):
	initial_layer = create_layer(1)
	next_layer = create_layer(3)
	return first_val_larger_helper(target_value, initial_layer, 3, next_layer)

print(first_val_larger(target))

