from given_inputs import day_12a_test as input_str
from functools import reduce

def connected_programs(program_ls, prev_seen):
    if program_ls == []:
        return []
    else:
        not_seen = map(lambda x: x not in prev_seen, program_ls)
        trawl = lambda seen, p: seen + connected_programs(register[p], seen)
        all_seen = reduce(trawl, not_seen, prev_seen)
        return all_seen

register = {}
for line in input_str.splitlines():
    program = line.split(" <-> ")[0]
    incident_programs = line.split(" <-> ")[1].split(", ")
    register[program] = incident_programs
connected_to_zero = connected_programs(register['0'], ['0'])
print(len(connected_to_zero))
