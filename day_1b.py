from given_inputs import day_1b_final

arr = [int(i) for i in list(day_1b_final)]
inteval = len(arr) // 2
total = 0

for i in range(len(arr)):
	next_index = (i + inteval) % len(arr)
	if arr[i] == arr[next_index]:
		total += arr[i]

print(total)
