from given_inputs import day_11a_final as input_str

def get_dir_count(direction):
    if direction not in dir_counts:
        dir_counts[direction] = 0
    return dir_counts[direction]

def reduce_two_directions(dir1, dir2):
    min_count = min(get_dir_count(dir1), get_dir_count(dir2))
    dir_counts[dir1] = get_dir_count(dir1) - min_count
    dir_counts[dir2] = get_dir_count(dir2) - min_count
    return min_count

def merge(dir1, dir2, result_dir):
    init = get_dir_count(result_dir)
    dir_counts[result_dir] = init + reduce_two_directions(dir1, dir2)

def remove_opp_dir():
    reduce_two_directions("n", "s")
    reduce_two_directions("nw", "se")
    reduce_two_directions("ne", "sw")

def merge_directions():
    merge("ne", "nw", "n")
    merge("se", "sw", "s")
    merge("se", "n", "ne")
    merge("sw", "n", "nw")
    merge("ne", "s", "se")
    merge("nw", "s", "sw")

dir_counts = {}
for direction in input_str.split(","):
    if direction not in dir_counts:
        dir_counts[direction] = 0
    dir_counts[direction] += 1
print("init", dir_counts)
remove_opp_dir()
print("removed opp", dir_counts)
merge_directions()
print("merged", dir_counts)
print(sum(dir_counts.values()))
