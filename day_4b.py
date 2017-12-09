from given_inputs import day_4b_final

passcode_strings = day_4b_final.splitlines()
all_passcodes = [passcode_str.split() for passcode_str in passcode_strings]
all_sorted_passcodes = [["".join(sorted(word)) for word in word_ls] for word_ls in all_passcodes]
valid_passcode_count = 0
for passcode in all_sorted_passcodes:
	if len(passcode) == len(set(passcode)):
		valid_passcode_count += 1
print(valid_passcode_count)