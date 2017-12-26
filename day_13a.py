from given_inputs import day_13a_test as input_str

def caught(depth, rng):
    depth += 1
    scanner_depth = (depth % ((rng * 2) - 1))
    if scanner_depth > rng:
        scanner_depth = rng - (scanner_depth % rng)
    return scanner_depth == 1

lines = input_str.splitlines()
severity = 0
for line in input_str.splitlines():
    depth = int(line.split(": ")[0])
    scan_range = int(line.split(": ")[1])
    if caught(depth, scan_range):
        severity += (depth * scan_range)
print(severity)
