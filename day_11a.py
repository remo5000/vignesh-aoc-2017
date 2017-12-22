from given_inputs import day_11a_final as input_str

def get_dir_count(direction, dir_counts):
    if direction not in dir_counts:
        dir_counts[direction] = 0
    return dir_counts[direction]

def reduce_two_directions(dir1, dir2, dir_counts):
    min_count = min(get_dir_count(dir1, dir_counts), get_dir_count(dir2, dir_counts))
    dir_counts[dir1] = get_dir_count(dir1, dir_counts) - min_count
    dir_counts[dir2] = get_dir_count(dir2, dir_counts) - min_count
    return min_count

def merge(dir1, dir2, result_dir, dir_counts):
    init = get_dir_count(result_dir, dir_counts)
    dir_counts[result_dir] = init + reduce_two_directions(dir1, dir2, dir_counts)

def remove_opp_dir(dir_counts):
    reduce_two_directions("n", "s", dir_counts)
    reduce_two_directions("nw", "se", dir_counts)
    reduce_two_directions("ne", "sw", dir_counts)

def merge_directions(dir_counts):
    merge("ne", "nw", "n", dir_counts)
    merge("se", "sw", "s", dir_counts)
    merge("se", "n", "ne", dir_counts)
    merge("sw", "n", "nw", dir_counts)
    merge("ne", "s", "se", dir_counts)
    merge("nw", "s", "sw", dir_counts)

def total_distance(dir_counts):
    return sum(dir_counts.values())

dir_counts = {}
for direction in input_str.split(","):
    if direction not in dir_counts:
        dir_counts[direction] = 0
    dir_counts[direction] += 1
remove_opp_dir(dir_counts)
merge_directions(dir_counts)
print(total_distance(dir_counts))
