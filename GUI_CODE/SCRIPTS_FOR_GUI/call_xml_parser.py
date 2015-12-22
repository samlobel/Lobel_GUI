import os
from os.path import join



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
	if not os.path.isfile(full_path_to_xml):
		print "XML ISN'T FILE"
		return "XML ISN'T A FILE"
	if not full_path_to_xml.endswith('.xml'):
		print "XML FILENAME DOES NOT END WITH .xml"
		return "XML FILENAME DOES NOT END WITH .xml"
	if not os.path.isfile(full_path_to_genefile):
		print "GENEFILE ISN'T FILE"
		return "GENEFILE ISN'T FILE"
	label_mass = convert_reporter_to_label_mass(reporter_type)
	if not label_mass:
		print "bad label mass returned"
		return "reporter type not valid"
	xml_dir_name = full_path_to_xml.partition('.xml')[0]
	xml_dir_name = join(xml_dir_name, '')
	if os.path.isdir(xml_dir_name):
		print "xml directory already exists here, if you don't need it anymore try deleting it and running again"
		return "xml directory already exists here, if you don't need it anymore try deleting it and running again"
	os.mkdir(xml_dir_name)
	print "created xml directory"

	try:
		float(error_threshold)
	except:
		return "error threshold could not be parsed into a float"

	perl_call = "perl " + join(this_dir, 'parse_xtandem_sam.pl') + ' '+\
		full_path_to_xml + ' ' + xml_dir_name + ' ' + str(error_threshold) + ' ' +\
		str(label_mass) + ' ' + full_path_to_genefile

	print perl_call

	a = os.system(perl_call)
	if a:
		return "ERROR PARSING XML IN PERL SCRIPT"
	else:
		return 0


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

