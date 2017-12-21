from given_inputs import day_9a_final as input_str

total_score = 0
current_nest_score = 0
ignore_next = False
inside_garbage = False
for char in input_str:
	if ignore_next:
		ignore_next = False
	elif char == "!":
		ignore_next = True
	elif inside_garbage and char != ">":
		continue
	elif char == "<":
		inside_garbage = True
	elif char == ">":
		inside_garbage = False
	elif char == "{":
		current_nest_score += 1
	elif char == "}":
		total_score += current_nest_score
		current_nest_score -=1

print(total_score)