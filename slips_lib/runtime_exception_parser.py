import sys
import traceback

def get_error_line_number():
	exc_type, exc_value, exc_traceback = sys.exc_info()
	line_no = traceback.extract_tb(exc_traceback, -1)[0].lineno
	del(exc_type)
	del(exc_value)
	del(exc_traceback)
	return line_no

def get_error_line(source_code, line_no):
	lines = source_code.split('\n')
	source_line = lines[line_no -1]	
	return source_line
