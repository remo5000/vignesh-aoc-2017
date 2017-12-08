from given_inputs import day_4a_final

all_passcodes = [passcode_string.split() for passcode_string in day_4a_final.splitlines()]
valid_passcode_count = 0
for passcode in all_passcodes:
	word_dict = {}
	valid = True
	for word in passcode:
		if word in word_dict:
			valid = False
			break
		else:
			word_dict[word] = 0
	if valid:
		valid_passcode_count += 1
print(valid_passcode_count)
