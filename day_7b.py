from given_inputs import day_7b_test

# DATA STRUCTURE EMULATED
# {
#	name: (weight, list_of_children)	
# } 
programs = {}
lines = day_7b_test.splitlines()
# a line is name (weight)
#		 or name (weight) -> children
for line in lines:
	name = line.split(' ', 1)[0]
	weight = int(line.split('(')[1].split(')')[0])
	children = []
	if '->' in line:
		children = line.split('-> ')[1].split(', ')
	programs[name] = (weight, children)

parent = 
