import os

def select_only_one(mgf_read_path, mgf_write_path, mz_error, reporter_type, min_intensity, min_reporters):
	print "Selecting only one"
	perl_call = 'perl /Users/samlobel/Code/DAD/Lobel_GUI/GUI_CODE/SCRIPTS_FOR_GUI/mgf_select_only_one.pl '+\
	mgf_read_path + " " + mgf_write_path + " " + str(mz_error) + " " +\
	reporter_type + " " + str(min_intensity) + " " + str(min_reporters)
	print perl_call
	a = os.system(perl_call)
	# if a != 0:
	return a

def test_drive():
	print "GREAT JOB SUCCESS NOW"
	return "Good job very nice"
