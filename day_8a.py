from given_inputs import day_8a_final as input_str
import operator

def get_value(name):
	if name not in register:
		register[name] = 0
	return register[name]

def operate(operation):
	name, operator, operand = operation[0], operation[1], operation[2]
	if operator == "inc":
		register[name] = get_value(name) + operand
	elif operator == "dec":
		register[name] = get_value(name) - operand
	else:
		print("error: unknown operator @ function operate")

def condition_true(condition):
	name, operator, operand = condition[0], condition[1], condition[2]
	if operator == "<":
		return get_value(name) < operand
	elif operator == ">":
		return get_value(name) > operand
	elif operator == ">=":
		return get_value(name) >= operand
	elif operator == "<=":
		return get_value(name) <= operand
	elif operator == "==":
		return get_value(name) == operand
	elif operator == "!=":
		return get_value(name) != operand
	else:
		print("error: unknown operator @ function condition_true")

def parse_condition(line):
	line = line.split(' if ')[1].split(' ')
	line[2] = int(line[2])
	return line

def parse_operation(line):
	line = line.split(' if ')[0].split(' ')
	line[2] = int(line[2])
	return line

def largest_register_val(register):
	return max(list(register.values()))

register = {}

for line in input_str.splitlines():
	condition = parse_condition(line)
	operation = parse_operation(line)
	if condition_true(condition):
		operate(operation)

print(largest_register_val(register))
