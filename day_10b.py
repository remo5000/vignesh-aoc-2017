from given_inputs import day_10b_test as input_str
from day_10a import swap, reverse_subarray

sparse_hash = arr = list(range(256))
raw_index = 0
lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
skip_size = 0
for x in range(64):
    for reverse_length in lengths:
        start = raw_index % len(arr)
        print(arr, "reverse from", start, "length", reverse_length)
        reverse_subarray(arr, start, reverse_length)
        raw_index += reverse_length + skip_size
        skip_size += 1
print(arr)
