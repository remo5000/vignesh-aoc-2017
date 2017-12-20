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

def have_seen_before(arr, xs):
    return ",".join([str(i) for i in arr]) in xs

def add_to_seen_before(arr, xs):
    xs.add(",".join([str(i) for i in arr]))