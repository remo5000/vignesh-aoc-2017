from given_inputs import day_12a_final as input_str
from functools import reduce

def connected_programs_helper(program_ls, prev_seen, register):
    if len(program_ls) == 0:
        return set()
    else:
        prev_seen = prev_seen | set(program_ls)
        directly_connected = map(lambda x: register[x], program_ls)
        directly_connected = reduce(lambda a, x: a + x, directly_connected, [])
        unseen = list(set(directly_connected) - prev_seen)
        return prev_seen | connected_programs_helper(unseen, prev_seen, register)

def connected_programs(first_program, register):
    program_ls = register[first_program]
    prev = set([first_program])
    return connected_programs_helper(program_ls, prev, register)

register = {}
for line in input_str.splitlines():
    program = line.split(" <-> ")[0]
    incident_programs = line.split(" <-> ")[1].split(", ")
    register[program] = incident_programs
connected_to_zero = connected_programs('0', register)
print(connected_to_zero)
print(len(connected_to_zero))
