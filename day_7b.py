from given_inputs import day_7b_final
from day_7a import find_root
from collections import Counter

# DATA STRUCTURE EMULATED
# {
#	name: (weight, list_of_children)	
# } 

def get_program(name):
	return program_dict[name]

def get_weight(program):
	return program[0]

def has_children(program):
	return len(program[1]) > 0

def get_children(program):
	return program[1]

def child_count(program):
	return len(get_children(program))

def total_weight(program):
	weight = get_weight(program)
	if has_children(program):
		for child_str in get_children(program):
			weight += total_weight(get_program(child_str))
	return weight

def different_num_in_ls(ls):
	counts = dict(Counter(ls))
	for key, value in counts.items():
		if value == 1:
			return key
	return -1

def odd_program(program_ls, weight):
	for program in program_ls:
		if total_weight(program) == weight:
			return program

def weight_to_balance(parent, target_weight):
	if not has_children(parent):
		return target_weight
	else:
		children = get_children(parent)
		child_programs = list(map(get_program, children))
		child_weights = list(map(total_weight, child_programs))
		diff_weight = different_num_in_ls(child_weights)
		if diff_weight == -1:
			return target_weight - sum(child_weights)
		else:
			new_target_weight = (sum(child_weights) - diff_weight) // (child_count(parent) - 1)
			target_program = odd_program(child_programs, diff_weight)
			return weight_to_balance(target_program, new_target_weight)

program_dict = {}
input_str = day_7b_final
lines = input_str.splitlines()
for line in lines:
	name = line.split(' ', 1)[0].strip()
	weight = int(line.split('(')[1].split(')')[0])
	children = []
	if '->' in line:
		children = line.split('-> ')[1].split(', ')
	program_dict[name] = (weight, children)

root = find_root(input_str)
print(weight_to_balance(get_program(root), 0))
