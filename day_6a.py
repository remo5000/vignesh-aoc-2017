from given_inputs import day_6a_test

arr = [int(c) for c in  day_6a_test.split()]
previously_seen = {}
redist_count = 0
reached_infinite_loop = False

def max_element_index(arr):
    max_index = 0
    max_num = arr[max_index]
    for index, num in enumerate(arr):
        if num >= max_num:
            max_num = num
            max_index = index
    return max_index

def distribute(max_index, arr):
    print("max is", arr[max_index], "arr is", arr, "len is", len(arr)) 
    while arr[max_index] >= len(arr) - 1:
        for index in range(len(arr)):
            if index == max_index:
                continue
            else:
                arr[index] += 1
        # for index_to_add in range(max_index + 1, max_index + len(arr)):
        #     arr[index_to_add % len(arr)] += 1
        # arr[max_index] -= (len(arr) - 1)

def seen_before(arr):
    return ",".join([str(i) for i in arr]) in previously_seen

def add_to_seen_before(arr):
    previously_seen[",".join([str(i) for i in arr])] = True

add_to_seen_before(arr)
while not reached_infinite_loop:
    # print("array", arr, "previously_seen", previously_seen)    
    max_index = max_element_index(arr)
    distribute(max_index, arr)
    # print("after redist,", arr)
    redist_count += 1
    if seen_before(arr):
        print(arr, "is in", previously_seen)
        reached_infinite_loop = True
    else:
        add_to_seen_before(arr)

print(redist_count)
