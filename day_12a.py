from given_inputs import day_12a_final as input_str
from functools import reduce

def connected_programs_helper(program_ls, prev_seen):
    print("unseen", program_ls, "seen", prev_seen)
    programs = filter(lambda x: x not in prev_seen, program_ls)
    if len(program_ls) == 0:
        return set()
    else:
        trawl = lambda seen, p: seen | connected_programs_helper(register[p], seen | set([p]))
        all_seen = reduce(trawl, list(programs), prev_seen)
        return all_seen

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
