import os
from os.path import join
import shutil
from combine_xml_mgf import combine_parsed_xml_mgf 


def parse_xtandem(full_path_to_xml, threshold, label_mass_int, genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))

	full_path_to_genefile = join(this_dir, 'gene_files', genefile)

	# perl_call = "perl " + join(this_dir, 'parse_xtandem_lobel.pl') + ' '+\
	# 	full_path_to_xml + ' ' + str(threshold) + ' ' + str(label_mass_int) + ' ' +\
	# 	full_path_to_genefile

	# print perl_call

	if not os.path.isfile(full_path_to_xml):
		print "XML ISN'T FILE"
		return "XML ISN'T A FILE"
	if not full_path_to_xml.endswith('.xml'):
		print "XML FILENAME DOES NOT END WITH .xml"
		return "XML FILENAME DOES NOT END WITH .xml"
	if not os.path.isfile(full_path_to_genefile):
		print "GENEFILE ISN'T FILE"
		return "GENEFILE ISN'T FILE"
	
	perl_call = "perl " + join(this_dir, 'parse_xtandem_sam.pl') + ' '+\
		full_path_to_xml + ' ' + str(threshold) + ' ' + str(label_mass_int) + ' ' +\
		full_path_to_genefile
	print perl_call
	a = os.system(perl_call)
	if a:
		return "ERROR PARSING XML IN PERL SCRIPT"
	else:
		return 0


def parse_xtandem_new(full_path_to_xml, error_threshold, reporter_type, genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))
	full_path_to_genefile = join(this_dir, 'gene_files', genefile)
	# if not os.path.isfile(full_path_to_xml):
	# 	print "XML ISN'T FILE"
	# 	return "XML ISN'T A FILE"
	# if not full_path_to_xml.endswith('.xml'):
	# 	print "XML FILENAME DOES NOT END WITH .xml"
	# 	return "XML FILENAME DOES NOT END WITH .xml"
	# if not os.path.isfile(full_path_to_genefile):
	# 	print "GENEFILE ISN'T FILE"
	# 	return "GENEFILE ISN'T FILE"

	# going on the assumption it's been validated

	label_mass = convert_reporter_to_label_mass(reporter_type)
	if not label_mass:
		print "bad label mass returned"
		return "reporter type not valid"
	# xml_dir_name = full_path_to_xml.partition('.xml')[0]
	# xml_dir_name = join(xml_dir_name, '')
	xml_dir_name = xml_dirname_from_filename(full_path_to_xml)
	if os.path.isdir(xml_dir_name):
		print "xml directory already exists here, if you don't need it anymore try deleting it and running again"
		return "xml directory already exists here, if you don't need it anymore try deleting it and running again"

	xml_txt_filename = full_path_to_xml + '.txt'
	if os.path.isfile(xml_txt_filename):
		print "xml txt file already exists there, either you've already run this in the past or you have a residual file you don't want. Consider deleting or moving that file"
		return "xml txt file already exists there, either you've already run this in the past or you have a residual file you don't want. Consider deleting or moving that file"

	os.mkdir(xml_dir_name)
	print "created xml directory"

	# try:
	# 	float(error_threshold)
	# except:
	# 	return "error threshold could not be parsed into a float"

	perl_call = "perl " + join(this_dir, 'parse_xtandem_sam.pl') + ' '+\
		full_path_to_xml + ' ' + xml_dir_name + ' ' + str(error_threshold) + ' ' +\
		str(label_mass) + ' ' + full_path_to_genefile

	print perl_call

	a = os.system(perl_call)
	if a:
		return "ERROR PARSING XML IN PERL SCRIPT"
	else:
		print "no error in perl script, all good."
		return 0
		# print "no error in perl script. Should delete the xml directory, because we don't need it anymore, just keep the xml.txt"
		# try:
		# 	shutil.rmtree(xml_dir_name)
		# 	return 0
		# except:
		# 	print "trouble deleting the directory afterwards."
		# 	return "Trouble deleting xml directory afterwards"
			# This is safe because it'll only delete the directory that you create.
			# But still, something to be careful about in the future, in case I forget
			# and change something
		# return 0


def parse_xtandem_combine_with_mgf(full_path_to_xml, error_threshold, reporter_type, genefile, selected_mgfdir):
	resp = parse_xtandem_new(full_path_to_xml, error_threshold, reporter_type, genefile)
	if resp:
		print "from parse_xtandem_combine_with_mgf, error detected in parse_xtandem_new: " + str(resp)
		return resp
	print "stop here for now"
	return 0

	xml_dir_name = xml_dirname_from_filename(full_path_to_xml)
	resp_2 = combine_parsed_xml_mgf(selected_mgfdir, xml_dir_name, reporter_type)
	if resp_2:
		print "from parse_xtandem_combine_with_mgf, error in combine_parsed_xml_mgf: " + str(resp_2)
		return resp_2

	print "Looks good, cleaning up xml directory."
	try:
		shutil.rmtree(xml_dir_name)
		print "directory cleaned, well done"
		return 0
	except:
		print "trouble deleting the directory afterwards."
		return "Trouble deleting xml directory afterwards"

	# return 0






def xml_dirname_from_filename(full_path_to_xml):
	almost_xml_dir_name = full_path_to_xml.partition('.xml')[0]
	xml_dir_name = join(almost_xml_dir_name, '')
	return xml_dir_name


def convert_reporter_to_label_mass(reporter):
	mapping = {
		'TMT0' : '225',
		'TMT2' : '225',
		'TMT6' : '229',
		'TMT10' : '229',
		'iTRAQ4' : '144',
		'iTRAQ8': '304'
	}
	if reporter not in mapping:
		return None
	return mapping[reporter]

