import copy
from given_inputs import day_6b_final as input_str
from day_6_func_defs import *

arr = [int(c) for c in  input_str.split()]
previously_seen = set()
reached_infinite_loop = False
repeated_state = ""
add_to_seen_before(arr, previously_seen)

while not reached_infinite_loop:
    distribute(arr)
    if have_seen_before(arr, previously_seen):
        reached_infinite_loop = True
        repeated_state = arr.copy()
    else:
        add_to_seen_before(arr, previously_seen)

reached_infinite_loop = False
counter = 0
while not reached_infinite_loop:
    print(arr)
    distribute(arr)
    counter += 1
    if arr == repeated_state and counter != 0:
        reached_infinite_loop = True

print(counter)