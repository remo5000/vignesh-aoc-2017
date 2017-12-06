from given_inputs import day_2b_final

def first_quotient(ls):
	ls = sorted(ls)
	for i in range(len(ls)):
		divisor = ls[i]
		for dividend in ls[i + 1:]:
			if dividend % divisor == 0:
				return dividend // divisor
	return 0

list_of_strings = day_2b_final.splitlines()
char_lists = [i.split() for i in list_of_strings]
matrix = [[int(char) for char in char_ls] for char_ls in char_lists]
quotients = list(map(first_quotient, matrix))
print(sum(quotients))