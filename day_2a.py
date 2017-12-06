from given_inputs import day_2a_final

def checksum(ls):
	smallest = largest = ls[0]
	for num in ls:
		if num < smallest:
			smallest = num
		elif num > largest:
			largest = num
	return largest - smallest

list_of_strings = day_2a_final.splitlines()
char_lists = [i.split() for i in list_of_strings]
matrix = [[int(char) for char in char_ls] for char_ls in char_lists]
checksums = list(map(checksum, matrix))
print(sum(checksums))