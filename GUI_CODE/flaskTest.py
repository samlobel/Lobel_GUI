from flask import Flask, render_template, request
app = Flask(__name__)
from time import time
from SCRIPTS_FOR_GUI import mgf_select_one
from SCRIPTS_FOR_GUI import helper
import json
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


	# a = mgf_select_one.test_drive()

	# print "From test drive:" + a
	
	return "LOOKS GOOD HOMIE"


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

