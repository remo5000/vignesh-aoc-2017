from given_inputs import day_6a_final as input_str
from day_6_func_defs import *

arr = [int(c) for c in  input_str.split()]
previously_seen = set()
reached_infinite_loop = False
add_to_seen_before(arr, previously_seen)

while not reached_infinite_loop:
    distribute(arr)
    if have_seen_before(arr, previously_seen):
        reached_infinite_loop = True
    else:
        add_to_seen_before(arr, previously_seen)

print(len(previously_seen))