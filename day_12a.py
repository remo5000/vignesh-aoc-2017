from given_inputs import day_12a_final as input_str
from functools import reduce

def connected_programs_helper(program_ls, prev_seen):
    if len(program_ls) == 0:
        return set()
    else:
        prev_seen = prev_seen | set(program_ls)
        connected_programs = map(lambda x: register[x], program_ls)
        connected_programs = reduce(lambda a, x: a + x, connected_programs, [])
        unseen_programs = list(set(connected_programs) - prev_seen)
        return prev_seen | connected_programs_helper(unseen_programs, prev_seen)

def connected_programs(first_program):
    return connected_programs_helper(register[first_program], set([first_program]))

register = {}
for line in input_str.splitlines():
    program = line.split(" <-> ")[0]
    incident_programs = line.split(" <-> ")[1].split(", ")
    register[program] = incident_programs
connected_to_zero = connected_programs('0')
print(connected_to_zero)
print(len(connected_to_zero))
