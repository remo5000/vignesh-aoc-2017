from given_inputs import day_5a_final

instructions = [int(c) for c in day_5a_final.splitlines()]
pointer = 0
steps = 0
while pointer < len(instructions):
	steps += 1
	displacement = instructions[pointer]
	instructions[pointer] += 1
	pointer += displacement
print(steps)
