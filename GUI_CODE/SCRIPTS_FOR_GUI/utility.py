import re
import os

def validate_float(num):
	strnum = str(num)
	matched = re.match('^\-?\d+\.?\d*$', strnum)
	return matched
	# pass


def validate_int(num):
	# pass
	strnum = str(num)
	matched = re.match('^\-?\d+$', strnum)
	return matched

def validate_ion_type(ion_type):
	possibilities = ['iTRAQ4','iTRAQ8','TMT10','TMT2','TMT6','TMT0']
	return (ion_type in possibilities)


def validate_gene_file(genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))
	genefile_fullpath = os.path.join(this_dir, 'gene_files', genefile)
	return os.path.isfile(genefile_fullpath)


def validate_error_input(error_input):
	strnum = str(error_input)
	re_1 = '^\d+\.?\d*$'
	re_2 = '^\d+\.?\d*[eE]\-\d+'
	return (re.match(re_1, strnum) or re.match(re_2, strnum))









def tests():
	assert validate_float('-0.5')
	assert not validate_float('--0.5')
	assert not validate_float('-.')
	assert not validate_float('-')
	assert not validate_float('-2.a0')
	assert validate_float('0.5')
	assert validate_float('10.')
	assert not validate_float('.5')
	assert validate_int('123')
	assert validate_int('-123')
	assert not validate_int('--123')
	assert not validate_int('123.5')
	assert not validate_int('123a')
	assert not validate_float('')
	assert not validate_int('')
	assert validate_error_input('1e-10')
	assert validate_error_input('1E-10')
	assert validate_error_input('5e-10')
	assert validate_error_input('1.e-10')
	assert not validate_error_input('.5e-10')
	assert validate_error_input('60.1234234')
	assert not validate_error_input('-5')
	assert not validate_error_input('-0.005')
	assert not validate_error_input('-2e6')
	assert not validate_error_input('-2')
	
	
	
	# Good, that actually helped me catch an error, well done sammy boy


# tests()

