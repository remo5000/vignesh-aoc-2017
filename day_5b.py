from given_inputs import day_5b_final

instructions = [int(c) for c in day_5b_final.splitlines()]
pointer = 0
steps = 0
while pointer < len(instructions):
	steps += 1
	displacement = instructions[pointer]
	instructions[pointer] += 1 if displacement < 3 else -1
	pointer += displacement
print(steps)
