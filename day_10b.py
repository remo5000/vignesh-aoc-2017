from given_inputs import day_10b_final as input_str
from day_10a import swap, reverse_subarray
import numpy
from functools import reduce

def XOR(ls):
    return reduce((lambda x, y: x ^ y), ls)

sparse_hash = arr = list(range(256))
raw_index = 0
lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
skip_size = 0
print(arr)
for x in range(64):
    for reverse_length in lengths:
        start = raw_index % len(arr)
        print(arr, "reverse from", start, "length", reverse_length)
        reverse_subarray(arr, start, reverse_length)
        raw_index += reverse_length + skip_size
        skip_size += 1
sparse_split = list(numpy.split(numpy.array(sparse_hash), 16))
dense_hash = [XOR(sixteen_num_ls) for sixteen_num_ls in sparse_split]
hex_hash = [hex(i).split('x')[1].zfill(2) for i in dense_hash]
print("".join(hex_hash))
