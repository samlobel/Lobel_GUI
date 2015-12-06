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



@app.route("/tab_1_function", methods=['POST'])
def tab_1_function():
	# print request.form
	# print request.args
	mgf_read_path = str(request.form['mgfReadPath'])
	print mgf_read_path
	mgf_write_path = str(request.form['mgfWritePath'])
	print mgf_write_path
	mz_error = str(request.form['mzError']);
	print mz_error
	reporter_type = str(request.form['reporterType'])
	print reporter_type
	min_reporters = str(request.form['minReporters'])
	print min_reporters
	min_intensity = str(request.form['minIntensity'])
	print min_intensity
	error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, mz_error, reporter_type, min_intensity, min_reporters)
	print "ERROR " + str(error)


@app.route("/tab_2_helper_function", methods=['POST'])
def tab_2_helper_function():
	mgf_read_dir_path = str(request.form['mgfReadDirPath'])
	# print mgf_read_dir_path
	if not os.path.isdir(mgf_read_dir_path):
		return "mgf read directory path is not a directory", 500
	mgf_write_dir_path = str(request.form['mgfWriteDirPath'])
	# print mgf_write_dir_path
	if not os.path.isdir(mgf_write_dir_path):
		return "mgf write directory path is not a directory", 500
	mgf_file_name = str(request.form['mgfFileName'])	
	print mgf_file_name
	mgf_read_path = join(mgf_read_dir_path, mgf_file_name)
	if not os.path.isfile(mgf_read_path):
		return "no file at specified path", 500
	mgf_write_path = join(mgf_write_dir_path, mgf_file_name)
	print mgf_write_path
	try:
		mz_error = str(int(request.form['mzError']));
	except:
		return "mz_error must be an integer", 500
	reporter_type = str(request.form['reporterType'])
	if not reporter_type:
		return "reporter type not specified", 500
	try:
		min_reporters = str(int(request.form['minReporters']))
	except:
		return "min_reporters must be an integer", 500
	try:
		min_intensity = str(int(request.form['minIntensity']))
	except:
		return "min_reporters must be an integer", 500
	error = mgf_select_one.select_only_one(mgf_read_path, mgf_write_path, mz_error, reporter_type, min_intensity, min_reporters)
	if error:
		return error, 500
	else:
		return "LOOKS GOOD HOMIE"

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
	# print threshold
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
	return "Badabadabing"



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
	# validate directory here
	pass

def validate_ion_type(ion_type):
	possibilities = ['iTRAQ4','iTRAQ8','TMT10','TMT2','TMT6']
	return (ion_type in possibilities)

# print validate_ion_type('iTRAQ4')




@app.route("/testRoutes", methods=['GET'])
def testRoutes():
	return science.function_one()


if __name__ == "__main__":
  app.run()

