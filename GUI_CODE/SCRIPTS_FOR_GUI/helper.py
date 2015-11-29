import os

def get_mgf_files_given_directory(directory):
	mgf_array = []
	for f in os.listdir(directory):
		if f.endswith(".mgf"):
			mgf_array.append(f)
	return mgf_array
