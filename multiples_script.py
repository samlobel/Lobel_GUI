import os

def check_file_for_duplicates(filename):
	scan_set = set()
	duplicates_set = set()
	for line in open(filename, "r"):
		if line.startswith("SCANS"):
			linelist = line.split('=')
			if linelist[1] not in scan_set:
				scan_set.add(linelist[1])
			else:
				if linelist[1] not in duplicates_set:
					duplicates_set.add(linelist[1])
	return duplicates_set

def check_files_for_duplicates(directoryname, suffix, write_to):
	file_to_write = open(write_to, 'w')
	for filename in os.listdir(directoryname):
		if filename.endswith(suffix):
			print "checking filename " + filename
			duplicate_set = check_file_for_duplicates(directoryname + '\\' + filename)
			if duplicate_set:
				print "FOUND"
				file_to_write.write(filename)
				file_to_write.write('\n')
				for dup in duplicate_set:
					file_to_write.write(dup)
				file_to_write.write('\n')
	file_to_write.close()

check_files_for_duplicates(".\\DATA_TestTMT2\\testAB\\selected-d20-TMT2-1000-2", '.mgf', 'multiples-selected.txt')