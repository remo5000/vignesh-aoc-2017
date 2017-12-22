from given_inputs import day_11b_final as input_str
from day_11a import remove_opp_dir, merge_directions, total_distance, get_dir_count

dir_counts = {}
furthest_step_count = 0
for direction in input_str.split(","):
    dir_counts[direction] = get_dir_count(direction, dir_counts) + 1
    remove_opp_dir(dir_counts)
    merge_directions(dir_counts)
    furthest_step_count = max(furthest_step_count, total_distance(dir_counts))
print(furthest_step_count)
