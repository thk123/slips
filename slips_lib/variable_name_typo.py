import nltk
import re
import ast

from slips_lib.friendly_errors import print_code
from slips_lib.friendly_errors import print_bad_code
import slips_lib.runtime_exception_parser

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

def get_variable_name(name_error):
	name_match = re.search('name \'(\w+)\' is not defined', str(name_error))
	variable_name = name_match.group(1)
	return variable_name

def run(name_error, file_path, soure_code, ast_value):
	error_line_no = slips_lib.runtime_exception_parser.get_error_line_number()
	source_line = slips_lib.runtime_exception_parser.get_error_line(soure_code, error_line_no)

	variable_name = get_variable_name(name_error)
	find_assignments = FindAssignments(variable_name)
	find_assignments.visit(ast_value)
	if len(find_assignments.best_guess) > 0: 
		print('typo in variable name \'' + variable_name + '\'')
		print_bad_code(source_line, source_line.find(variable_name), len(variable_name))
		
		print("Suggestion - replace with \'" + find_assignments.best_guess + '\':')
		print_code(source_line.replace(variable_name, find_assignments.best_guess))
