from flask import Flask, render_template, request
app = Flask(__name__)
from time import time
from SCRIPTS_FOR_GUI import mgf_select_one
from SCRIPTS_FOR_GUI import helper
import json
from os.path import join
from SCRIPTS_FOR_GUI import combine_selected_mgf_files
from SCRIPTS_FOR_GUI import call_xml_parser
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
	return render_template(file_name)


@app.route("/combine_mgf_files", methods=['POST'])
def combine_mgf_files():
	print "combine_mgf_files"
	mgf_read_path = str(request.form['mgfWriteDirPath'])
	mgf_write_path = join(mgf_read_path, "MERGED.mgf")
	combine_selected_mgf_files.concat_mgf_files_given_dirname(mgf_write_path, mgf_read_path)
	return "GOOD JOB DOOD"
	
@app.route("/combine_mgf_txt_files", methods=['POST'])
def combine_mgf_txt_files():
	print "combine_mgf_txt_files"
	mgf_read_path = str(request.form['mgfWriteDirPath'])
	mgf_write_path = join(mgf_read_path, "MERGED.mgf.txt")
	combine_selected_mgf_files.concat_mgf_txt_files_given_dirname(mgf_write_path, mgf_read_path)
	return "GOOD JOB DOOD"



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
	print mgf_read_dir_path
	mgf_write_dir_path = str(request.form['mgfWriteDirPath'])
	print mgf_write_dir_path
	mgf_file_name = str(request.form['mgfFileName'])
	print mgf_file_name
	mgf_read_path = join(mgf_read_dir_path, mgf_file_name)
	print mgf_read_path
	mgf_write_path = join(mgf_write_dir_path, mgf_file_name)
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


	# a = mgf_select_one.test_drive()

	# print "From test drive:" + a
	
	return "LOOKS GOOD HOMIE"

@app.route("/tab_3_function", methods=['POST'])
def tab_3_function():
	print "HANDLE TAB 3"
	xml_read_path = str(request.form['xmlReadPath'])
	print xml_read_path
	threshold = int(request.form['threshold'])
	threshold = str(round(threshold / 100.0, 2))
	print threshold
	labelMass = str(request.form['labelMass'])
	print labelMass
	geneFile = str(request.form['geneFile'])
	print geneFile
	# return "Looking Good"
	a = call_xml_parser.parse_xtandem(xml_read_path, threshold, labelMass, geneFile)
	to_return =  "Return from parse_xtandem: " + str(a)
	print to_return
	return to_return



@app.route("/getMGFFiles", methods=['POST'])
def getMGFFiles():
	print "GET MGF FILES"
	mgf_read_dir_path = str(request.form['mgfReadDirPath'])
	print "Got past read dir path"
	files = helper.get_mgf_files_given_directory(mgf_read_dir_path)
	print "Files"
	print files
	text = json.dumps(files)
	return text



@app.route("/submitForm", methods=['POST'])
def submitForm():
	t_1 = time()
	while time() - t_1 < 1:
		i = 0

	print "yoyoyo"
	# return {'html' : "<div>Submitted</div>"}
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

