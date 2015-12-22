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
	





# def tests():
# 	assert validate_float('-0.5')
# 	assert not validate_float('--0.5')
# 	assert not validate_float('-.')
# 	assert not validate_float('-')
# 	assert not validate_float('-2.a0')
# 	assert validate_float('0.5')
# 	assert validate_float('10.')
# 	assert not validate_float('.5')
# 	assert validate_int('123')
# 	assert validate_int('-123')
# 	assert not validate_int('--123')
# 	assert not validate_int('123.5')
# 	assert not validate_int('123a')
# 	assert not validate_float('')
# 	assert not validate_int('')
# 	# Good, that actually helped me catch an error, well done sammy boy


# tests()

