from given_inputs import day_13a_final as input_str

# 6 4   m3
def caught(depth, rng):
    max_rng = rng - 1
    scanner_depth = depth % ((rng * 2) - 1)
    if scanner_depth > max_rng:
        excess = scanner_depth - max_rng
        scanner_depth = max_rng - excess
    return scanner_depth == 0

lines = input_str.splitlines()
severity = 0
for line in input_str.splitlines():
    depth = int(line.split(": ")[0])
    scan_range = int(line.split(": ")[1])
    if caught(depth, scan_range):
        print(depth, scan_range)
        severity += (depth * scan_range)
print(severity)
