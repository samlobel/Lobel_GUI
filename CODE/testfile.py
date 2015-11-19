import sys, os

def add_a_or_b_label_to_sorted_mfg_txt_file(filename):
	a = open(filename, "r")
	temp_filename = filename + "_PLACEHOLDER"
	temp_file = open(temp_filename, "w")

	first_line = a.readline()
	temp_file.write(first_line.strip() + "\tduplicate_flag\n")
	first_line_arr = first_line.split('\t')
	filename_index = first_line_arr.index("filename")
	scan_index = first_line_arr.index("scan")
	if scan_index == -1 or filename_index == -1:
		raise Exception("something is wrong with the file formatting")
	scan_list = []
	first = True
	most_recent = (None, None)
	for line in a:
		line_arr = line.split("\t")
		curr_scan = line_arr[scan_index]
		curr_filename = line_arr[filename_index]
		tup = (curr_filename, curr_scan)
		# print tup
		# if first == 1 or (most_recent == tup):
			# scan_list.append(line)
		print str(most_recent[1]) + " : " + str(tup[1])
		if (not first) and (not (most_recent[1] == tup[1])):
			if len(scan_list) == 0:
				raise Exception("Something is funky, shouldn't be zero")
			elif len(scan_list) == 1:
				temp_file.write(scan_list[0].strip() + "\tA\n")
			else:
				print "printing b!"
				for l in scan_list:
					temp_file.write(l.strip() + "\tB\n")
			scan_list = []
		else:
			print "not going in to the thing"
		scan_list.append(line)
		most_recent == tup
		first = False
	if len(scan_list) == 0:
		raise Exception("Something is funky, shouldn't be zero")
	elif len(scan_list) == 1:
		temp_file.write(scan_list[0].strip() + "\tA\n")
	else:
		for l in scan_list:
			temp_file.write(l.strip() + "\tB\n")
	print "Complete!1!1!"
	a.close()
	temp_file.close()
	os.remove(filename)
	os.rename(temp_filename,filename)

# REMEMBER TO DO ONE AT THE END TOO!
add_a_or_b_label_to_sorted_mfg_txt_file(sys.argv[1])