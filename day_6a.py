from given_inputs import day_6a_final as input_str

def max_element_index(arr):
    return arr.index(max(arr))

def brute_distribute(max_index, arr):
    i = max_index
    max_val = arr[i]
    while max_val:
        i = (i + 1) % len(arr)
        arr[i] += 1
        max_val -= 1
    arr[max_index] = max_val

def distribute(max_index, arr):
    max_val = arr[max_index]
    increment = max_val // (len(arr) - 1)
    max_val = max_val % (len(arr) - 1)
    for i in range(len(arr)):
        if i == max_index:
            arr[i] = max_val
        else:
            arr[i] += increment
    brute_distribute(max_index, arr)

def have_seen_before(arr):
    return ",".join([str(i) for i in arr]) in previously_seen

def add_to_seen_before(arr):
    previously_seen.add(",".join([str(i) for i in arr]))

arr = [int(c) for c in  input_str.split()]
previously_seen = set()
reached_infinite_loop = False
add_to_seen_before(arr)

while not reached_infinite_loop:
    max_index = max_element_index(arr)
    distribute(max_index, arr)
    if have_seen_before(arr):
        reached_infinite_loop = True
    else:
        add_to_seen_before(arr)

print(len(previously_seen))