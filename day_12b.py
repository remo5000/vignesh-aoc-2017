from given_inputs import day_12b_final as input_str
from functools import reduce
from day_12a import connected_programs

def number_of_groups(register):
    key_ls = list(register.keys())
    if len(key_ls) == 0:
        return 0
    else:
        first_program = key_ls[0]
        group = list(connected_programs(first_program, register))
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
