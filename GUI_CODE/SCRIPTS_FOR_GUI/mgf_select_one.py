import os
from os.path import join

def select_only_one(mgf_read_path, mgf_write_path, mz_error, reporter_type, min_intensity, min_reporters):
	print "Selecting only one"
	this_dir = os.path.dirname(os.path.realpath(__file__))
	perl_call = 'perl ' + join(str(this_dir), 'mgf_select_only_one.pl') + ' '+\
	mgf_read_path + " " + mgf_write_path + " " + str(mz_error) + " " +\
	reporter_type + " " + str(min_intensity) + " " + str(min_reporters)
	print perl_call
	a = os.system(perl_call)
	# if a != 0:
	return a

def test_drive():
	print "GREAT JOB SUCCESS NOW"
	return "Good job very nice"
