from given_inputs import day_4a_final

all_passcodes = [passcode_string.split() for passcode_string in day_4a_final.splitlines()]
valid_passcode_count = 0

for passcode in all_passcodes:
	if len(passcode) == len(set(passcode)):
		valid_passcode_count += 1

# # Dictionary Method
# for passcode in all_passcodes:
# 	word_dict = {}
# 	valid = True
# 	for word in passcode:
# 		if word in word_dict:
# 			valid = False
# 			break
# 		else:
# 			word_dict[word] = 0
# 	if valid:
# 		valid_passcode_count += 1

# # Naive Method
# for passcode in all_passcodes:
# 	print(passcode)
# 	valid = True
# 	for word in passcode:
# 		passcode.remove(word)
# 		if word in passcode:
# 			valid = False
# 			break
# 	if valid:
# 		valid_passcode_count += 1

print(valid_passcode_count)

