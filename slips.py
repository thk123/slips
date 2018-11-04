#!/usr/bin/env python

from slips_lib.run_checks import run_checks
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: lips program_to_check.py')
		exit(1)

	file_path = sys.argv[1]

	with open(sys.argv[1]) as source_file:
		soure_code = source_file.read()

		run_checks(file_path, soure_code)
