from flask import Flask, render_template, request
app = Flask(__name__)
from time import time
from SCRIPTS_FOR_GUI import mgf_select_one
from SCRIPTS_FOR_GUI import helper
import json
from os.path import join
from SCRIPTS_FOR_GUI import combine_selected_mgf_files
from SCRIPTS_FOR_GUI import call_xml_parser
import os
from SCRIPTS_FOR_GUI import combine_xml_mgf
import math
# from science_code import science

@app.route("/")
def main():
	# print render_template('index.html')
	return render_template('index_new.html')

@app.route("/tab", methods=['GET'])
def tab():
	# tab_num = request.args.get('num')
	# file_name = "tab_" + str(tab_num) + ".html"
	# print file_name
	file_name = str(request.args.get('name')) + '.html'
	# print "fetching gene_files"
	gene_files = helper.get_gene_files_array()
	inverse_files = helper.get_inverse_files_array()
	# print gene_files
	return render_template(file_name, gene_files=gene_files,\
	 inverse_files=inverse_files)


@app.route("/combine_mgf_files", methods=['POST'])
def combine_mgf_files():
	print "combine_mgf_files"
	mgf_read_path = str(request.form['mgfWriteDirPath'])
	merged_dir = join(mgf_read_path, "MERGED")
	print merged_dir
	if not os.path.exists(merged_dir):
		print "Going to make a directory now"
		os.mkdir(merged_dir)
		print "Directory Made"
	else:
		print "Path exists already?"

	mgf_write_path = join(merged_dir, "MERGED.mgf")

	print "MGFWRITEPATH: " + str(mgf_write_path)
	error = combine_selected_mgf_files.concat_mgf_files_given_dirname(mgf_write_path, mgf_read_path)
	if error:
		return error, 500
	else:
		return "Combined"
	
@app.route("/combine_mgf_txt_files", methods=['POST'])
def combine_mgf_txt_files():
	print "combine_mgf_txt_files"
	mgf_read_path = str(request.form['mgfWriteDirPath'])
	merged_dir = join(mgf_read_path, "MERGED")
	print merged_dir
	if not os.path.exists(merged_dir):
		os.mkdir(merged_dir)

	mgf_write_path = join(merged_dir, "MERGED.mgf.txt")
	error = combine_selected_mgf_files.concat_mgf_txt_files_given_dirname(mgf_write_path, mgf_read_path)
	# return "GOOD JOB DOOD"
	if error:
		return error, 500
	else:
		return "Combined"

@app.route("/tab_5_helper_function", methods=['POST'])
def tab_5_helper_function():
	# pass
	# If it gets here, we assume that there are mgf.txt files in the
	# right place. We should do a check anyways, but we can assume because
	# of how we get here.
	
	return "not yet implemented", 500



# @app.route("/tab_1_function", methods=['POST'])
# def tab_1_function():
# 	# print request.form
# 	# print request.args
# 	mgf_read_path = str(request.form['mgfReadPath'])
# 	print mgf_read_path
# 	mgf_write_path = str(request.form['mgfWritePath'])
# 	print mgf_write_path
# 	mz_error = str(request.form['mzError']);
# 	print mz_error
# 	reporter_type = str(request.form['reporterType'])
# 	print reporter_type
# 	min_reporters = str(request.form['minReporters'])
# 	print min_reporters
# 	min_intensity = str(request.form['minIntensity'])
# 	print min_intensity
# 	should_select = str(request.form['shouldPerformMGFSelection'])
# 	error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, \
# 	 	mz_error, reporter_type, min_intensity, min_reporters, should_select)
# 	print "ERROR " + str(error)


# def check_for_good_input_tab_two(form):





# @app.route("/tab_2_make_sure_dirs_dont_exist", methods=["POST"])
# def tab_2_make_sure_dirs_dont_exist():
# 	mgf_read_dir_path = str(request.form['mgfReadDirPath'])
# 	should_select = str(request.form['mgfOperationToPerform'])

# 	mgf_txt_write_dir_path = join(mgf_read_dir_path, 'selected_mgf_txt', '')
# 	# if os.path.isdir()

@app.route("/tab_2_helper_function", methods=['POST'])
def tab_2_helper_function():
	# return "trial by fire", 500
	# print str(request.form)
	# return "Form printed, that's all we want right now"

	# First, figure out which operation we want to perform.
	print "trying out arguments"
	print str(request.form)
	perform_recalibration = str(request.form['performRecalibration'])
	print "through first two"
	should_select = str(request.form['mgfOperationToPerform'])
	print "after should_select"


	mgf_read_dir_path = str(request.form['mgfReadDirPath'])
	mgf_file_name = str(request.form['mgfFileName'])
	reporter_type = str(request.form['reporterIonType'])
	min_intensity = str(int(request.form['minIntensity']))
	min_reporters = str(int(request.form['minReporters']))
	# should_select = str(request.form['shouldPerformMGFSelection'])

	print "through next oens"


	mz_error = str(int(request.form['mzError']))

	mz_error_initial_run = str(int(request.form['mzErrorInitialRun']));
	mz_error_recalibration = str(int(request.form['mzErrorRecalibration']));

	print "mz_errors parsed"



	print "got through everything"
	print "now checking general inputs"

	mgf_read_path = join(mgf_read_dir_path, mgf_file_name)


	if should_select != "0" and should_select != "1":
		return "could not determine whether to select from mgf file, ask Sam", 500

	if not os.path.isdir(mgf_read_dir_path):
		return "mgf read directory path is not a directory", 500

	if not os.path.isfile(mgf_read_path):
		print "mgf path does not lead to file"
		return "mgf_path does not lead to a file", 500

	mgf_txt_write_dir_path = join(mgf_read_dir_path, 'selected_mgf_txt', '')
	# mgf_write_path = join(mgf_write_dir_path, mgf_file_name)
	# mgf_txt_write_path = join(mgf_txt_write_dir_path, mgf_file_name + '.txt')	

	print "created paths"
	
	mgf_txt_write_path = 'placeholder'
	mgf_write_path = 'placeholder'

	try:
		os.makedirs(mgf_txt_write_dir_path)
	except:
		print "mgf.txt directory probably already there"
	if not os.path.isdir(mgf_txt_write_dir_path):
		return "selected_mgf_txt directory could not be created", 500
	mgf_txt_write_path = join(mgf_txt_write_dir_path, mgf_file_name + '.txt')

	if should_select == '1':
		mgf_write_dir_path = join(mgf_read_dir_path, 'selected_mgf', '')
		try:
			os.makedirs(mgf_write_dir_path)
		except:
			print "mgf directory probably already there"
		if not os.path.isdir(mgf_write_dir_path):
			return "selected_mgf directory could not be created", 500	
		mgf_write_path = join(mgf_write_dir_path, mgf_file_name)

	print "checking general inputs"

	# reporter_type = str(request.form['reporterType'])
	if not reporter_type:
		return "reporter type not specified", 500
	# I should also check to make sure it's one of the ones we want.
	# if  reporter_type 
	# valid_reporter_types = ['TMT0','TMT2','TMT6','TMT10','iTRAQ4','iTRAQ8']
	if not validate_ion_type(reporter_type):
		return "reporter type not a valid choice", 500

	if perform_recalibration == '1':
		first_val = int(mz_error_initial_run)
		second_val = int(mz_error_recalibration)
		if math.isnan(first_val) or math.isnan(second_val):
			return "One of your mz_errors isn't a number", 500
		if first_val < second_val:
			return "recalibration error must be smaller than initial error", 500
		print "parsing, recalibrating"
		error = mgf_select_one.select_only_one_recalibrate(mgf_read_path, mgf_write_path, mgf_txt_write_path, \
			mz_error_initial_run, reporter_type, min_intensity, min_reporters, should_select, mz_error_recalibration)
		if error:
			print "bad bad bad"
			return error, 500
		else:
			return "Looking good."

	elif perform_recalibration == '0':
		first_val = int(mz_error)
		if math.isnan(first_val):
			return "mz error isn't a number", 500
		print "parsing, not recalibrating"
		error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, mgf_txt_write_path, \
			mz_error, reporter_type, min_intensity, min_reporters, should_select)
		if error:
			print "bad bad bad"
			return error, 500
		else:
			return "Looking good"
	else:
		return "Trouble determining whether to recalibrate, ask Sam", 500

	# print "running function"
	# if perform_recalibration == '1':
	# 	# check inputs

	# 	pass
	# elif perform_recalibration == '0':
	# 	pass
	# else:
	# 	return "Trouble determining whether to recalibrate, ask Sam", 500


	# mgf_read_dir_path = str(request.form['mgfReadDirPath'])
	# if not os.path.isdir(mgf_read_dir_path):
	# 	return "mgf read directory path is not a directory", 500
	# mgf_write_dir_path = join(mgf_read_dir_path, 'selected_mgf')
	# mgf_txt_write_dir_path = join(mgf_read_dir_path, 'selected_mgf_txt')
	# mgf_file_name = str(request.form['mgfFileName'])
	# reporter_type = str(request.form['reporterType'])
	# min_intensity = str(int(request.form['minIntensity']))
	# min_reporters = str(int(request.form['minReporters']))
	# should_select = str(request.form['shouldPerformMGFSelection'])

	# mgf_read_path = join(mgf_read_dir_path, mgf_file_name)
	# mgf_write_path = join(mgf_write_dir_path, mgf_file_name)
	# mgf_txt_write_path = join(mgf_txt_write_dir_path, mgf_file_name + '.txt')

	# mz_error = str(int(request.form['mzError']))

	# mz_error_initial_run = str(int(request.form['mzErrorInitialRun']));
	# mz_error_recalibration = str(int(request.form['mzErrorRecalibration']));

	
	# print "got through everything"
	# try:
	# 	os.makedirs(mgf_txt_write_dir_path)
	# except:
	# 	print "mgf.txt directory probably already there"
	# if should_select == '1':
	# 	try:
	# 		os.makedirs(mgf_write_dir_path)
	# 	except:
	# 		print "mgf directory probably already there"
	# # print "made directories, about to do the processing."
	# # print mgf_read_path
	# # print mgf_write_path
	# # print mgf_txt_write_path
	# # print mz_error
	# # print reporter_type
	# # print min_intensity
	# # print min_reporters
	# # print should_select

	# print "running function"
	# error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, mgf_txt_write_path, \
	# 	mz_error, reporter_type, min_intensity, min_reporters, should_select)
	# if error:
	# 	print "bad bad bad"
	# 	return error, 500
	# else:
	# 	return "LOOKING GOOD HERE"




# @app.route("/OLD_tab_2_helper_function", methods=['POST'])
# def OLD_tab_2_helper_function():
# 	mgf_read_dir_path = str(request.form['mgfReadDirPath'])
# 	# print mgf_read_dir_path
# 	if not os.path.isdir(mgf_read_dir_path):
# 		return "mgf read directory path is not a directory", 500
# 	mgf_write_dir_path = str(request.form['mgfWriteDirPath'])
# 	# print mgf_write_dir_path
# 	if not os.path.isdir(mgf_write_dir_path):
# 		return "mgf write directory path is not a directory", 500
# 	mgf_file_name = str(request.form['mgfFileName'])
# 	print mgf_file_name
# 	mgf_read_path = join(mgf_read_dir_path, mgf_file_name)
# 	if not os.path.isfile(mgf_read_path):
# 		return "no file at specified path", 500
# 	mgf_write_path = join(mgf_write_dir_path, mgf_file_name)
# 	print mgf_write_path
# 	try:
# 		mz_error = str(int(request.form['mzError']));
# 	except:
# 		return "mz_error must be an integer", 500
# 	reporter_type = str(request.form['reporterType'])
# 	if not reporter_type:
# 		return "reporter type not specified", 500
# 	try:
# 		min_reporters = str(int(request.form['minReporters']))
# 	except:
# 		return "min_reporters must be an integer", 500
# 	try:
# 		min_intensity = str(int(request.form['minIntensity']))
# 	except:
# 		return "min_reporters must be an integer", 500
# 	try:
# 		should_select = str(request.form['shouldPerformMGFSelection'])
# 		print "Should select: " + str(should_select)
# 		if should_select == None:
# 			return "shouldPerformMGFSelection was None", 500
# 		if not (should_select == '1' or should_select == '0'):
# 			return "shouldPerformMGFSelection not either 0 or 1", 500
# 	except:
# 		return "Missing shouldPerformMGFSelection", 500

# 	error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, \
# 		mz_error, reporter_type, min_intensity, min_reporters, should_select)

# 	if error:
# 		return error, 500
# 	else:
# 		return "LOOKS GOOD HOMIE"

@app.route("/tab_3_function", methods=['POST'])
def tab_3_function():
	print "HANDLE TAB 3"
	xml_read_path = str(request.form['xmlReadPath'])
	# print xml_read_path
	try:
		threshold = int(request.form['threshold'])
		threshold = str(round(threshold / 100.0, 2))
	except ValueError:
		print "bad threshold value"
		return "ERROR: Bad Threshold Value", 500
	try:
		labelMass = str(int(request.form['labelMass']))
	except ValueError:
		print "bad labelMass value"
		return "ERROR: Bad Label Mass Value", 500
	# print labelMass
	geneFile = str(request.form['geneFile'])
	a = call_xml_parser.parse_xtandem(xml_read_path, threshold, labelMass, geneFile)
	to_return =  "Return from parse_xtandem: " + str(a)
	if a:
		return a, 500
	print to_return
	return to_return

@app.route("/combine_parsed_xml_with_parsed_mgf", methods=["POST"])
def combine_parsed_xml_with_parsed_mgf():
	print "COMBINING PARSED XML WITH PARSED MGF"
	mgf_selected_path = request.form['mgfSelectedPath']
	if not mgf_selected_path:
		return "Error: mgf_selected_path is required", 500
	if not os.path.isdir(mgf_selected_path):
		return "Error: mgf_selected_path is not a directory", 500
	xml_directory_path = request.form['xmlDirectoryPath']
	if not xml_directory_path:
		return "Error: xml_directory_path is required", 500
	if not os.path.isdir(xml_directory_path):
		return "Error: mgf_selected_path is not an existing directory", 500
	reporter_type = request.form['reporterIonType']
	if not reporter_type:
		return "Error: No reporter-type specified", 500
	print "All good so far"
	a = combine_xml_mgf.combine_parsed_xml_mgf(mgf_selected_path, xml_directory_path, reporter_type)
	if a:
		print a
		return a, 500
	return "Looking good"



@app.route("/getMGFFiles", methods=['POST'])
def getMGFFiles():
	try:
		mgf_read_dir_path = str(request.form['mgfReadDirPath'])
		files = helper.get_mgf_files_given_directory(mgf_read_dir_path)
		text = json.dumps(files)
		return text
	except:
		return "ERROR FETCHING MGF FILES", 500



@app.route("/submitForm", methods=['POST'])
def submitForm():
	t_1 = time()
	while time() - t_1 < 1:
		i = 0

	print "yoyoyo"
	return "<div>Hello you</div>"	

@app.route("/secondSubmit", methods=['POST'])
def secondSubmit():

	t_1 = time()
	while time() - t_1 < 2:
		i = 0
	print "oyoyoyo"
	# return {'html' : "<div>Submitted</div>"}
	return "<div>Goodbye you</div>"


def validate_directory(dirname):
	pass

def validate_ion_type(ion_type):
	possibilities = ['iTRAQ4','iTRAQ8','TMT10','TMT2','TMT6','TMT0']
	return (ion_type in possibilities)




if __name__ == "__main__":
  app.run(processes=8)
  # app.run()

