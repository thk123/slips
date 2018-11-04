def print_code(code):
	print('\t' + code)

def print_bad_code(code, start_pos, length):
	print_code(code)
	print_code((" " * start_pos) + ("~" * length))