from flask import Flask, render_template, request
app = Flask(__name__)
from time import time
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

