from utility import *


def validate_tab_2(request):
	print "validating tab_2"
	try:
		mgf_read_dir_path = str(request.form['mgfReadDirPath'])
		mgf_file_name = str(request.form['mgfFileName'])
		reporter_type = str(request.form['reporterIonType'])
		min_intensity = str(int(request.form['minIntensity']))
		min_reporters = str(int(request.form['minReporters']))

		perform_recalibration = str(request.form['performRecalibration'])
		should_select = str(request.form['mgfOperationToPerform'])

		mz_error = str(int(request.form['mzError']))

		mz_error_initial_run = str(int(request.form['mzErrorInitialRun']));
		mz_error_recalibration = str(int(request.form['mzErrorRecalibration']));

		if not os.path.isdir(mgf_read_dir_path):
			print "mgf read directory path is not a directory"
			return False, "mgf read directory path is not a directory"

		if not mgf_file_name.endswith('.mfg'):
			print "mgf file name doesn't end with .mgf, that's fishy"
			return False, "mgf file name doesn't end with .mgf, that's fishy"

		if not validate_ion_type(reporter_type):
			print "not a valid ion type"
			return False, "not a valid ion type"

		if not validate_int(min_reporters):
			print "min reporters is not a valid int"
			return False, "min reporters is not a valid int"

		if not validate_int(min_intensity):
			print "min intensity is not a valid int"
			return False, "min intensity is not a valid int"



		if perform_recalibration != "0" and perform_recalibration != "1":
			print "could not determine whether to perform recalibration"
			return False, "could not determine whether to perform recalibration"

		if perform_recalibration == "0" and not validate_int(mz_error):
			print "mz_error not valid int"
			return False, "mz_error not valid int"

		if perform_recalibration == "1":
		 	if not validate_int(mz_error_initial_run):
				print "mz_error initial not valid int"
				return False, "mz_error initial not valid int"
			if not validate_int(mz_error_recalibration):
				print "mz_error recalibration not valid int"
				return False, "mz_error recalibration not valid int"



		if should_select != "0" and should_select != "1":
			print "could not determine whether to select from mgf file, ask Sam"
			return False, "could not determine whether to select from mgf file, ask Sam"

		# I'll make the directories later, this isn't the place for that. Or, maybe it is.
		# Maybe I should make them somewhere else, and check here.

		mgf_read_path = join(mgf_read_dir_path, mgf_file_name)

		if not os.path.isfile(mgf_read_path):
			print "mgf path does not lead to file"
			return False, "mgf_path does not lead to a file"

		return True

	except:
		print "Missing form input"
		return False, "Missing form input"


def validate_tab_5(request):
	print "validating tab_5"
	try:
		xml_read_path = request.form['xmlReadPath']
		threshold = request.form['threshold']
		reporter_type = request.form['reporter_type']
		geneFile = request.form['geneFile']

		if not xml_read_path or str(threshold) or reporter_type or geneFile:
			print "Missing form input (one is blank)"
			return False, "Missing form input (one is blank)"

		if not xml_read_path.endswith('.xml'):
			print "xml file doesn't end with .xml, that's fishy"
			return False, "xml file doesn't end with .xml, that's fishy"

		if not os.path.isfile(xml_read_path):
			print "could not open xml file at that path"
			return False, "could not open xml file at that path"

		if not validate_float(threshold):
			print "threshold must be a decimal"
			return False, "threshold must be a decimal"

		if not validate_ion_type(reporter_type):
			print "Invalid reporter type"
			return False, "Invalid reporter type"

		# this_dir = os.path.dirname(os.path.realpath(__file__))
		if not validate_gene_file(geneFile):
			print "invalid gene file"
			return False, "Invalid gene file"

		return True
		
	except:
		print "Missing form input"
		return False, "Missing form input"



