from given_inputs import day_7a_final

def find_root(input):
	names = [line.split(' ', 1)[0] for line in input.splitlines()]
	number_of_parents = {name: 0 for name in names}
	for line in input.splitlines():
		if '->' not in line:
			continue
		children = line.split('-> ')[1].split(', ')
		for child in children:
			number_of_parents[child] += 1
	for program in number_of_parents:
		if number_of_parents[program] == 0:
			return program

print(find_root(day_7a_final))
