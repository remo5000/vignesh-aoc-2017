from given_inputs import day_9b_final as input_str

total_score = 0
current_nest_score = 0
ignore_next = False
inside_garbage = False
garbage_count = 0
for char in input_str:
	if ignore_next:
		ignore_next = False
	elif char == "!":
		ignore_next = True
	elif inside_garbage and char != ">":
		garbage_count += 1
		continue
	elif char == "<":
		inside_garbage = True
	elif char == ">":
		inside_garbage = False

print(garbage_count)