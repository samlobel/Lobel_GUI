import os
from os.path import join



def parse_xtandem(full_path_to_xml, threshold, label_mass_int, genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))
	full_path_to_genefile = join(this_dir, 'gene_files', genefile)

	perl_call = "perl " + join(this_dir, 'parse_xtandem_lobel.pl') + ' '+\
		full_path_to_xml + ' ' + str(threshold) + ' ' + str(label_mass_int) + ' ' +\
		full_path_to_genefile

	print perl_call

	if not os.path.isfile(full_path_to_xml):
		print "XML ISN'T FILE"
		return 1
	if not full_path_to_xml.endswith('.xml'):
		print "XML FILENAME DOES NOT END WITH .xml"
	if not os.path.isfile(full_path_to_genefile):
		print "GENEFILE ISN'T FILE"
		return 1
	
	perl_call = "perl " + join(this_dir, 'parse_xtandem_sam.pl') + ' '+\
		full_path_to_xml + ' ' + str(threshold) + ' ' + str(label_mass_int) + ' ' +\
		full_path_to_genefile
	print perl_call
	a = os.system(perl_call)
	return a
# parse_xtandem("/Users/samlobel/String", 1, 300, "RAT75_PTGN.txt")

