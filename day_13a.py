from given_inputs import day_13a_final as input_str

def caught(depth, rng):
    scanner_depth = depth % (rng + 2)
    max_rng_index = rng - 1
    if scanner_depth > max_rng_index:
        scanner_depth = max_rng_index - (scanner_depth % max_rng_index)
    return scanner_depth == 0

lines = input_str.splitlines()
depth_range_map = {}
for line in input_str.splitlines():
    depth = int(line.split(": ")[0])
    rng = int(line.split(": ")[1])
    depth_range_map[depth] = rng

severity = 0
for depth, scan_range in depth_range_map.items():
    if caught(depth, scan_range):
        severity += (depth * scan_range)
print(severity)
