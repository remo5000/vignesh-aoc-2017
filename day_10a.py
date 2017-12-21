from given_inputs import day_10a_final as input_str

def swap(arr, first, second):
    t = arr[first]
    arr[first] = arr[second]
    arr[second] = t

def reverse_subarray(arr, first_index, length):
    length -= 1
    middle_index = first_index + (length // 2)
    for i in range(first_index, middle_index + 1):
        displacement = i - first_index
        j = first_index + (length - displacement)
        i, j = i % len(arr), j % len(arr)
        swap(arr, i, j)

arr = list(range(256))
raw_index = 0
lengths = [int(c) for c in input_str.split(",")]
skip_size = 0
for reverse_length in lengths:
    start = raw_index % len(arr)
    print(arr, "reverse from", start, "length", reverse_length)
    reverse_subarray(arr, start, reverse_length)
    raw_index += reverse_length + skip_size
    skip_size += 1
print(arr)
print(arr[0] * arr[1])
