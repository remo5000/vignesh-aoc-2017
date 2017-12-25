from given_inputs import day_12b_final as input_str
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

def number_of_groups(register):
    key_ls = list(register.keys())
    if len(key_ls) == 0:
        return 0
    else:
        first_program = key_ls[0]
        group = list(connected_programs(first_program))
        for program in group:
            del register[program]
        return 1 + number_of_groups(register)

register = {}
for line in input_str.splitlines():
    program = line.split(" <-> ")[0]
    incident_programs = line.split(" <-> ")[1].split(", ")
    register[program] = incident_programs

group_count = number_of_groups(register)
print(group_count)
