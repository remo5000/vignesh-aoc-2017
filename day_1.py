from given_inputs import day1_final

arr = [int(i) for i in list(day1_final)]
total = 0

for i in range(len(arr)):
	next_index = 0 if i == len(arr) - 1 else i + 1
	if arr[i] == arr[next_index]:
		total += arr[i]

print(total)
