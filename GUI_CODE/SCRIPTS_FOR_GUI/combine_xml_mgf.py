from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import sys, os, shutil

from os.path import join


# get THIS directory! All of the initial files have got to be relative to this directory!
# this_dir = sys.path[0] + "\\"

this_dir = os.path.dirname(os.path.realpath(__file__))

print this_dir

# Assigns argument values to variables


# def check_if_mgf_select_already_executed(mgf_directory, mz_error, type, min_intensity, min_reporters):
# 	# mkdir(qq!$dir/selected-d$mz_error-$type-$min_intensity-$min_reporters/mgf-txt-files!);
# 	print "Checking if mgf_select_reporter.pl has already been called"
# 	for raw_mgf_file in os.listdir(mgf_directory):
# 		if raw_mgf_file.endswith('.mgf'):
# 			mgf_txt_file = '%s/selected-d%s-%s-%s-%s/mgf-txt-files/%s.txt' % (mgf_directory, mz_error, type, min_intensity, min_reporters, raw_mgf_file)
# 			print mgf_txt_file
# 			if not os.path.isfile(mgf_txt_file):
# 				print "%s has not been selected from" % (mgf_txt_file)
# 				return False
# 	print "All files have been selected from. NOT executing mgf_select_reporter.pl again."
# 	return True


def remove_duplicate_lines(filename):
	suffix = '_with_duplicates_removed'
	lines_seen = set()
	write_dest = filename + suffix
	# os.remove(outfile) # there were errors before because it was appending instead of overwriting.
	outfile = open(write_dest, "w")
	for line in open(filename, "r"):
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
		else:
			print "duplicate line removed: " + str(line)
	outfile.close()
	os.remove(filename)
	os.rename(write_dest, filename)


def clear_directory_of_files(directory):
	for item in os.listdir(directory):
		if os.path.isfile(item):
			toRemove = directory + '/' + item
			os.remove(directory + '/' + item)
			print toRemove + " removed"


# def remove_worse_error_scores(filename):
# 	file_scans_seen = set()
# 	duplicate_file_scans_seen = set()
	
# 	for line in open(filename, "r"):



def add_a_or_b_label_to_sorted_mfg_txt_file(filename):
	print "adding a and b labels "
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
		if (not first) and (not (most_recent[1] == tup[1])):
			if len(scan_list) == 0:
				raise Exception("Something is funky, shouldn't be zero")
			elif len(scan_list) == 1:
				temp_file.write(scan_list[0].strip() + "\tA\n")
			else:
				for l in scan_list:
					temp_file.write(l.strip() + "\tB\n")
			scan_list = []
		scan_list.append(line)
		most_recent = tup
		first = False
	if len(scan_list) == 0:
		raise Exception("Something is funky, shouldn't be zero")
	elif len(scan_list) == 1:
		temp_file.write(scan_list[0].strip() + "\tA\n")
	else:
		for l in scan_list:
			temp_file.write(l.strip() + "\tB\n")
	a.close()
	temp_file.close()
	os.remove(filename)
	os.rename(temp_filename,filename)

# REMEMBER TO DO ONE AT THE END TOO!


def add_c_labels_to_duplicate_marker_column(filename):
	print "adding c labels "
	a = open(filename, "r")
	temp_filename = filename + "_PLACEHOLDER"
	temp_file = open(temp_filename, "w")

	first_line = a.readline()
	temp_file.write(first_line)
	first_line_arr = first_line.split('\t')
	filename_index = first_line_arr.index("filename")
	scan_index = first_line_arr.index("scan")
	duplicate_index = first_line_arr.index("duplicate_flag")
	log_e_index = first_line_arr.index("log(e)") #Hopefully it's there
	if scan_index == -1 or filename_index == -1 or duplicate_index == -1 or log_e_index == -1:
		raise Exception("something is wrong with the file formatting")
	scan_list = []
	first = True
	most_recent = (None, None)
	for line in a:
		line_arr = line.split("\t")
		curr_scan = line_arr[scan_index]
		curr_filename = line_arr[filename_index]
		curr_duplicate_flag = line_arr[duplicate_index]
		tup = (curr_filename, curr_scan)
		if (not first) and (not (most_recent[1] == tup[1])):
			if len(scan_list) == 0:
				raise Exception("Something is funky, shouldn't be zero")
			elif len(scan_list) == 1:
				temp_file.write("\t".join(scan_list[0]))
			else:
				new_list = [(float(l[log_e_index]), l) for l in scan_list]
				new_list = sorted(new_list)
				for i in range(len(new_list)):
					arr = new_list[i][1]
					arr[duplicate_index] = "C" + str(i + 1)
					temp_file.write("\t".join(arr)) 
			scan_list = []
		scan_list.append(line_arr)
		most_recent = tup
		first = False
	if len(scan_list) == 0:
		raise Exception("Something is funky, shouldn't be zero")
	elif len(scan_list) == 1:
		temp_file.write("\t".join(scan_list[0]))
	else:
		new_list = [(float(l[log_e_index]), l) for l in scan_list]
		new_list = sorted(new_list)
		for i in range(len(new_list)):
			arr = new_list[i][1]
			arr[duplicate_index] = "C" + str(i + 1)
			temp_file.write("\t".join(arr)) 
	a.close()
	temp_file.close()
	os.remove(filename)
	os.rename(temp_filename,filename)

# REMEMBER TO DO ONE AT THE END TOO!




def take_in_file_sorted_by_filename_scan_output_file_with_duplicate_marker_column(filename):
	a = open(filename, "r")
	temp_file = open(filename + "_PLACEHOLDER", "w")
	
	first_line = a.readline()
	temp_file.write(first_line.strip() + "\tduplicate_flag\n")

	first_line_arr = first_line.split('\t')
	log_e_index = first_line_arr.index("log(e)") #Hopefully it's there
	scan_index = first_line_arr.index("scan")
	filename_index = first_line_arr.index("filename")
	if scan_index == -1 or filename_index == -1:
		raise Exception("something is wrong with the file formatting")
	scan_list = []
	curr_values = (None, None)
	for line in a:
		line_arr = line.split("\t")
		curr_scan = line_arr[scan_index]
		curr_log_e = float(line_arr[log_e_index])
		curr_filename = line_arr[filename_index]
		tup = (curr_filename, curr_scan)
		if curr_values == tup:
			print "dealing with duplicate! Line is as follows:"
			print line
			scan_list.append((log_e, line))
		else:
			scan_list = sorted(scan_list)
			lines = [elem[1] for elem in scan_list]
			if len(lines) == 0:
				raise Exception("length zero?")
			elif len(lines) == 1:
				for i in range(len(lines)):
					print "yo"
			else:
				print "yoda"







def remove_log_e_duplicates(filename):
	a = open(filename, "r")

	first_line = a.readline()
	first_line_arr = first_line.split('\t')
	log_e_index = first_line_arr.index("log(e)") #Hopefully it's there
	scan_index = first_line_arr.index("scan")

	scan_set = set()
	least_dict = {}
	duplicates_set = set()

	# reads rest of file
	for line in a:
		line_arr = line.split("\t")
		scan = line_arr[scan_index]
		log_e = float(line_arr[log_e_index])

		if scan not in scan_set:
			scan_set.add(scan)
			least_dict[scan] = log_e
		else: #we've seen it before
			least_dict[scan] = min(least_dict[scan], log_e)
			duplicates_set.add(scan) #find the smallest scan, add it to duplicates
		# Here, we've run through the file, found all the duplicates, found the smallest value.
		# Now, we just need to re-run through, writing the least only.

	a.close()
	a = open(filename, "r") #get to the beginning again
	tempdest = filename + "_with_duplicates_deleted" 
	# os.remove(tempdest)  # there were errors before because it was appending instead of overwriting. 
	b = open(tempdest, "w")

	first_line = a.readline()
	b.write(first_line)

	already_written = set() #this is a little annoying, but what if there's two things with the same
							#scan and the same error? Then we get duplicates. And certainty is worth speed.

	for line in a:
		line_arr = line.split("\t")
		scan = line_arr[scan_index]
		log_e = float(line_arr[log_e_index])

		if scan not in already_written:
			if log_e == least_dict[scan]:
				b.write(line)
				already_written.add(scan)
	b.close()
	a.close()

	os.remove(filename) #On windows you've got to remove the destination first.
	os.rename(tempdest, filename)








error=0
if len(sys.argv)>1:
	mgfdir = sys.argv[1]
if len(sys.argv)>2:
	xmlfile = sys.argv[2]
else:
	error=1
if len(sys.argv)>3:
	threshold = sys.argv[3]
else:
	threshold=1e-1
if len(sys.argv)>4:
	mz_error = int(sys.argv[4])
else:
	mz_error=20
if len(sys.argv)>5:
	type = sys.argv[5]
else:
	type='iTRAQ8'
if len(sys.argv)>6:
	min_intensity = sys.argv[6]
else:
	min_intensity=1000
if len(sys.argv)>7:
	min_reporters = sys.argv[7]
else:
	min_reporters=2
if len(sys.argv)>8:
	genefile=sys.argv[8]
else:
	genefile='RAT75_PTGN.txt'


# WE DON'T WANT TO RUN THIS IF WE ALREADY HAVE A GPM...... DIRECTORY (THAT MEANS WE'VE RUN THE PARSE THING ALREADY.)
first_part_of_xml_filename = xmlfile.rpartition('.')[0]
if os.path.isdir(first_part_of_xml_filename):
	print "The XML file you chose already has a directory associated with it, deleting it now so it can be recreated in parse_xtandem."
	# raise Exception("The XML file you chose already has a directory associated with it, running this here will cause problems.")
	shutil.rmtree(first_part_of_xml_filename)

		
print mgfdir + ' ' +xmlfile + ' ' + str(threshold) + ' ' + str(mz_error) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters) + ' ' + str(error)

if error==0:
	#make it work regardless of if the I is lowercase.
	if type=='ITRAQ4':
		type='iTRAQ4'

	if type=='ITRAQ8':
		type='iTRAQ8'


	if type=='iTRAQ8':
		start_col=type+'-113'
		end_col=type+'-121'
		label_mass_int=304
	if type=='iTRAQ4':
		start_col=type+'-114'
		end_col=type+'-117'
		label_mass_int=144
	if type=='TMT6':
		start_col=type+'-126'
		end_col=type+'-131'
		label_mass_int=229
	if type=='TMT10':
		start_col=type+'-126'
		end_col=type+'-131'
		label_mass_int=229
	if type=='TMT2':
		start_col=type+'-126'
		end_col=type+'-127'
		label_mass_int=225
	if type=='TMT0':
		start_col=type+'-126'
		end_col=type+'-126'
		label_mass_int=225

	# genes = pd.read_table(this_dir + 'RAT75_PTGN.txt',header=None,names=['protein','t','g','gene'],index_col=['protein'])
	# genes=genes.drop(['t','g'], axis=1)
	#print genes.loc['ENSRNOP00000000006'][0]
	print "about to execute parse_xtandem_lobel"
	os.system('perl ' + this_dir + 'parse_xtandem_lobel.pl ' + xmlfile + ' ' + str(threshold) + ' ' + str(int(label_mass_int)) + ' ' + this_dir + genefile)
	print "about to execute mgf_select_reporter"
	if not check_if_mgf_select_already_executed(mgfdir, mz_error, type, min_intensity, min_reporters):
		os.system('perl ' + this_dir + 'mgf_select_reporter.pl ' + mgfdir + ' ' + str(mz_error) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters))


	# os.system('perl mgf_select_reporter.pl ' + mgfdir+ '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal' + ' ' + str(mz_error) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters))
	# os.system('perl mgf_select_reporter.pl ' + mgfdir+ '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal' + ' ' + str(int(mz_error/2)) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters))
	# os.system('perl mgf_select_reporter.pl ' + mgfdir+ '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal' + ' ' + str(int(mz_error/4)) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters))
	corr = pd.read_table(this_dir + type + '-inv.txt')
	corr=corr.drop('Unnamed: 0', axis=1)
	xmldir,sep,ext = xmlfile.rpartition('.')
	for filename in os.listdir(xmldir):
		if filename.endswith('.mgf.txt'):
			print filename
			# drop the duplicates.
			xmlfilename = xmldir + '/' + filename
			# print "Dropping duplicates for " + xmlfilename
			# remove_log_e_duplicates(xmlfilename) #this funciton is only for the xml.txt file
			
			mgffilename = mgfdir + '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/mgf-txt-files/' + filename
			# print "dropping duplicates for " + mgffilename
			# remove_duplicate_lines(mgffilename)
			
			mgf = pd.read_table(mgffilename, index_col=['filename','scan','charge'])
			xml = pd.read_table(xmlfilename, index_col=['filename','scan','charge'])

			mgf.sort_index()

			testing_filename = mgffilename.split('.mgf.txt')[0] + '_duplicate_sorted' + '.mgf.txt'
			mgf.to_csv(testing_filename, sep='\t')
			add_a_or_b_label_to_sorted_mfg_txt_file(testing_filename)
			mgf = pd.read_table(testing_filename, index_col=['filename','scan','charge'])

			# dfc=pd.concat([mgf, xml], axis=1)
			dfc=pd.merge(mgf,xml, left_index=True, right_index=True)
			dfc_=dfc.dropna()
			csv_filename = xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table.txt'
			print "Writing to " + str(csv_filename)
			dfc_.to_csv(csv_filename,sep='\t')
			# add_c_labels_to_duplicate_marker_column(csv_filename)

			# mgf = pd.read_table(mgfdir + '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/' + filename, index_col=['filename','scan'])
			# dfc=pd.concat([mgf, xml], axis=1)
			# dfc_=dfc.dropna()
			# dfc_.to_csv(xmldir + '/' + filename + '_cal_' + str(mz_error) + '_table.txt',sep='\t')
			
			# mgf = pd.read_table(mgfdir + '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal/selected-d' + str(int(mz_error/2)) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/' + filename, index_col=['filename','scan'])
			# dfc=pd.concat([mgf, xml], axis=1)
			# dfc_=dfc.dropna()
			# dfc_.to_csv(xmldir + '/' + filename + '_cal_' + str(int(mz_error/2)) + '_table.txt',sep='\t')

			# mgf = pd.read_table(mgfdir + '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/reporter_cal/selected-d' + str(int(mz_error/4)) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/' + filename, index_col=['filename','scan'])
			# dfc=pd.concat([mgf, xml], axis=1)
			# dfc_=dfc.dropna()
			# dfc_.to_csv(xmldir + '/' + filename + '_cal_' + str(int(mz_error/4)) + '_table.txt',sep='\t')



			data = pd.read_table(xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table.txt')
			for k in range(len(data)):
				#print k,len(data),start_col,end_col,data
				#print data.ix[k,start_col:end_col]
				
				# this next line gets the kth row, and the start_col to end_col columns, which are strings like iTRAQ-115.
				
				temp=np.dot(data.ix[k,start_col:end_col].values,corr.values)
				# print "data: " + str(data.ix[k,start_col:end_col].values)
				# print "temp: " + str(temp)
				# print "corr: " + str(corr.values)
				temp=temp.astype(float)
				temp[temp<0]=0
				temp/=sum(temp)

				data.ix[k,start_col:end_col]=temp
			data.to_csv(xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table_corrected.txt',sep='\t',index=False)
			
			# data = pd.read_table(xmldir + '/' + filename + '_cal_' + str(mz_error) + '_table.txt')
			# for k in range(len(data)):
			# 	#print k,len(data),start_col,end_col,data
			# 	#print data.ix[k,start_col:end_col]
			# 	temp=np.dot(data.ix[k,start_col:end_col].values,corr.values)
			# 	temp=temp.astype(float)
			# 	temp[temp<0]=0
			# 	temp/=sum(temp)
			# 	data.ix[k,start_col:end_col]=temp
			# data.to_csv(xmldir + '/' + filename + '_cal_' + str(mz_error) + '_table_corrected.txt',sep='\t',index=False)
			
			# data = pd.read_table(xmldir + '/' + filename + '_cal_' + str(int(mz_error/2)) + '_table.txt')
			# for k in range(len(data)):
			# 	#print k,len(data),start_col,end_col,data
			# 	#print data.ix[k,start_col:end_col]
			# 	temp=np.dot(data.ix[k,start_col:end_col].values,corr.values)
			# 	temp=temp.astype(float)
			# 	temp[temp<0]=0
			# 	temp/=sum(temp)
			# 	data.ix[k,start_col:end_col]=temp
			# data.to_csv(xmldir + '/' + filename + '_cal_' + str(int(mz_error/2)) + '_table_corrected.txt',sep='\t',index=False)
			
			# data = pd.read_table(xmldir + '/' + filename + '_cal_' + str(int(mz_error/4)) + '_table.txt')
			# for k in range(len(data)):
			# 	#print k,len(data),start_col,end_col,data
			# 	#print data.ix[k,start_col:end_col]
			# 	temp=np.dot(data.ix[k,start_col:end_col].values,corr.values)
			# 	temp=temp.astype(float)
			# 	temp[temp<0]=0
			# 	temp/=sum(temp)
			# 	data.ix[k,start_col:end_col]=temp
			# data.to_csv(xmldir + '/' + filename + '_cal_' + str(int(mz_error/4)) + '_table_corrected.txt',sep='\t',index=False)
			
	first=1
	outfile_name = xmldir + '_nocal_' + str(mz_error) + '_table.txt'
	# os.remove(outfile_name) # there were errors before because it was appending instead of overwriting.
	with open(outfile_name, 'w') as outfile:
		for filename in os.listdir(xmldir):
			if filename.endswith('_nocal_' + str(mz_error) + '_table_corrected.txt'):
				with open(xmldir + '/' + filename) as infile:
					for line in infile:
						if (not 'other proteins' in line) or (first==1):
							first=0
							outfile.write(line)
	add_c_labels_to_duplicate_marker_column(outfile_name)
	print "Done!"



	# print "Deleting temporary xml txt file"
	# os.remove(xmldir + '.xml.txt')

	# print "Deleting temporary XML folder..."
	# shutil.rmtree(xmldir)

	# first=1
	# with open(xmldir + '_cal_' + str(mz_error) + '_table.txt', 'w') as outfile:
	# 	for filename in os.listdir(xmldir):
	# 		if filename.endswith('_cal_' + str(mz_error) + '_table_corrected.txt'):
	# 			with open(xmldir + '/' + filename) as infile:
	# 				for line in infile:
	# 					if (not 'other proteins' in line) or (first==1):
	# 						first=0
	# 						outfile.write(line)
						
	# first=1
	# with open(xmldir + '_cal_' + str(int(mz_error/2)) + '_table.txt', 'w') as outfile:
	# 	for filename in os.listdir(xmldir):
	# 		if filename.endswith('_cal_' + str(int(mz_error/2)) + '_table_corrected.txt'):
	# 			with open(xmldir + '/' + filename) as infile:
	# 				for line in infile:
	# 					if (not 'other proteins' in line) or (first==1):
	# 						first=0
	# 						outfile.write(line)
						
	# first=1
	# with open(xmldir + '_cal_' + str(int(mz_error/4)) + '_table.txt', 'w') as outfile:
	# 	for filename in os.listdir(xmldir):
	# 		if filename.endswith('_cal_' + str(int(mz_error/4)) + '_table_corrected.txt'):
	# 			with open(xmldir + '/' + filename) as infile:
	# 				for line in infile:
	# 					if (not 'other proteins' in line) or (first==1):
	# 						first=0
	# 						outfile.write(line)



def combine_parsed_xml_mgf(selected_mgfdir, xmldir, threshold, mz_error, reporter_ion_type, min_intensity, min_reporters, genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))
	if reporter_ion_type=='iTRAQ8':
		start_col=reporter_ion_type+'-113'
		end_col=reporter_ion_type+'-121'
		label_mass_int=304
	elif reporter_ion_type=='iTRAQ4':
		start_col=reporter_ion_type+'-114'
		end_col=reporter_ion_type+'-117'
		label_mass_int=144
	elif reporter_ion_type=='TMT10':
		start_col=reporter_ion_type+'-126'
		end_col=reporter_ion_type+'-131'
		label_mass_int=229
	else:
		raise Exception("Invalid reporter_ion_type")

	corr_path = join(this_dir, reporter_ion_type + "-inv.txt")
	if not os.path.isfile(corr_path):
		raise Exception("Cannot find correlation inverse matrix")
	corr = pd.read_table(corr_path)
	corr=corr.drop('Unnamed: 0', axis=1)
	# xmldir,sep,ext = xmlfile.rpartition('.')

	xmldir = join(xmldir,"")

	for filename in os.listdir(xmldir):
		if filename.endswith('.mgf.txt'):
			print filename
			xml_filename = join(xmldir, filename)
			mgf_txt_filename = join(selected_mgfdir, filename)
			xml = pd.read_table(xml_filename, index_col=['filename','scan','charge'])
			mgf = pd.read_table(mgf_txt_filename, index_col=['filename','scan','charge'])			
			mgf.sort_index()
			testing_filename = mgffilename.split('.mgf.txt')[0] + '_duplicate_sorted' + '.mgf.txt'
			mgf.to_csv(testing_filename, sep='\t')
			add_a_or_b_label_to_sorted_mfg_txt_file(testing_filename)
			mgf = pd.read_table(testing_filename, index_col=['filename','scan','charge'])

			dfc=pd.merge(mgf,xml, left_index=True, right_index=True)
			dfc_=dfc.dropna()
			csv_filename = xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table.txt'
			print "Writing to " + str(csv_filename)
			dfc_.to_csv(csv_filename,sep='\t')

			data = pd.read_table(xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table.txt')
			for k in range(len(data)):
				#print k,len(data),start_col,end_col,data
				#print data.ix[k,start_col:end_col]
				
				# this next line gets the kth row, and the start_col to end_col columns, which are strings like iTRAQ-115.
				
				temp=np.dot(data.ix[k,start_col:end_col].values,corr.values)
				# print "data: " + str(data.ix[k,start_col:end_col].values)
				# print "temp: " + str(temp)
				# print "corr: " + str(corr.values)
				temp=temp.astype(float)
				temp[temp<0]=0
				temp/=sum(temp)

				data.ix[k,start_col:end_col]=temp
			data.to_csv(xmldir + '/' + filename + '_nocal_table_corrected.txt',sep='\t',index=False)

	first=1
	outfile_name = xmldir + '_nocal_' + str(mz_error) + '_table.txt'
	# os.remove(outfile_name) # there were errors before because it was appending instead of overwriting.
	with open(outfile_name, 'w') as outfile:
		for filename in os.listdir(xmldir):
			if filename.endswith('_nocal_' + str(mz_error) + '_table_corrected.txt'):
				with open(xmldir + '/' + filename) as infile:
					for line in infile:
						if (not 'other proteins' in line) or (first==1):
							first=0
							outfile.write(line)
	add_c_labels_to_duplicate_marker_column(outfile_name)
	print "Done!"






	# I'm trying to make this function only do one thing, if I want more I can chain them with
	# async calls. So, I don't need a lot of this stuff.
	# mgf already selected from, xml is already processed. Just combine them here.

	








					
						