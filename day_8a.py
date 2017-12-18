from given_inputs import day_8a_test as input_str
import operator

def get_value(name):
	if name not in register:
		register[name] = 0
	return register[name]

def operate(name, operator, operand):
	if operator == "dec":
		operand *= -1
	register[name] = get_value(name) + operand

def condition_true(name, operator, operand):
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

def parse_condition(line):
	#TODO

def parse_operation(line):
	#TODO

register = {}

for line in input_str.splitlines():
	condition = parse_condition(line)
	if condition_true(condition[0], condition[1], condition[2]):
		operation = parse_operation(line)
		operate(operation[0], operation[1], operation[2])

print(max(stats.iteritems(), key=operator.itemgetter(1))[0])
