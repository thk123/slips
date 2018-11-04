import ast
import re
import sys
import traceback
import nltk

class FindAssignments(ast.NodeVisitor):
	var_name = ''
	best_distance = 0
	best_guess = ''
	def __init__(self, var_name):
		self.var_name = var_name
		self.best_distance = len(var_name) + 1

	def visit_Assign(self, node):
		for target in node.targets:
			if isinstance(target, ast.Name):
				target_name = target.id
				distance = nltk.edit_distance(target_name, self.var_name)
				if distance < self.best_distance:
					self.best_distance = distance
					self.best_guess = target_name


def run_checks(file_path, source_code):
	print('checking ' + file_path)

	ast_value = ast.parse(source_code, file_path)
	result = compile(source_code, file_path, 'exec')
	try:
		exec(result)
	except NameError as name_error:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = source_code.split('\n')
		line_no = traceback.extract_tb(exc_traceback, -1)[0].lineno
		source_line = lines[line_no -1]
		del(exc_type)
		del(exc_value)
		del(exc_traceback)
		name_match = re.search('name \'(\w+)\' is not defined', str(name_error))
		variable_name = name_match.group(1)
		find_assignments = FindAssignments(variable_name)
		find_assignments.visit(ast_value)
		if len(find_assignments.best_guess) > 0:
			start_pos = source_line.find(variable_name)
			print('typo in variable name \'' + variable_name + '\'')
			print('\t' + source_line + " (" + file_path + " line " + str(line_no) + ")")
			print('\t' + (" " * start_pos) + ("~" * len(variable_name)))
			print("Suggestion - replace with \'" + find_assignments.best_guess + '\':')
			print('\t' + source_line.replace(variable_name, find_assignments.best_guess))

