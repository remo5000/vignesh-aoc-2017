from given_inputs import day_1a_final

arr = [int(i) for i in list(day_1a_final)]
total = 0

for i in range(len(arr)):
	next_index = 0 if i == len(arr) - 1 else i + 1
	if arr[i] == arr[next_index]:
		total += arr[i]

print(total)
