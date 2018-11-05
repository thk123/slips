import ast
import slips_lib.variable_name_typo

def run_checks(file_path, source_code):
	print('checking ' + file_path)

	ast_value = ast.parse(source_code, file_path)
	result = compile(source_code, file_path, 'exec')
	try:
		exec(result)
	except NameError as name_error:
		slips_lib.variable_name_typo.run(name_error, file_path, source_code, ast_value)
		
		
