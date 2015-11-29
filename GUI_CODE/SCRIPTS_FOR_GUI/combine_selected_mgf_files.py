import shutil

def concat_mgf_files(output_filename, input_filename_array):
	with open(output_filename,'wb') as wfd:
		for f in input_filename_array:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd, 1024*1024*10)
				#10MB per writing chunk to avoid reading big file into memory.
	print "Concatenated"


from os import listdir
from os.path import isfile, join


def concat_mgf_files_given_dirname(output_filename, input_directory_name):
	filenames = [join(input_directory_name,f) for f in listdir(input_directory_name) if isfile(join(input_directory_name, f))]
	# return filenames
	concat_mgf_files(output_filename, filenames)

