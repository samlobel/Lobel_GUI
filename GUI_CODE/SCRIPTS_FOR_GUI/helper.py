import os

def get_mgf_files_given_directory(directory):
	mgf_array = []
	for f in os.listdir(directory):
		if f.endswith(".mgf"):
			mgf_array.append(f)
	return mgf_array


def get_gene_files_array():
	print "in get_gene_files_array"
	gene_file_array = []
	this_dir = os.path.dirname(os.path.realpath(__file__))
	print "before listdir"
	for f in os.listdir(os.path.join(this_dir, "gene_files")):
		print f
		if f.endswith('.txt'):
			gene_file_array.append(f)
	print "after listdir"
	return gene_file_array
