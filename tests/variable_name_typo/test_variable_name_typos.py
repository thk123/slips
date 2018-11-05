from subprocess import Popen, PIPE

def test_variable_name():
	process = Popen(["python3", "slips.py", "tests/variable_name_typo/wrong_named_variable.py"], stdout=PIPE)
	(output, err) = process.communicate()
	exit_code = process.wait()
	output_str = output.decode('utf-8')
	assert(output_str.find("typo in variable name 'varible'") != -1)
	assert(output_str.find("\tif varible == 5:") != -1)
	assert(output_str.find("Suggestion - replace with 'variable':") != -1)
