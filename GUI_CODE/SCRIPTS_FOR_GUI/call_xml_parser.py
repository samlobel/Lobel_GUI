import os
from os.path import join



def parse_xtandem(full_path_to_xml, threshold, label_mass_int, genefile):
	this_dir = os.path.dirname(os.path.realpath(__file__))
	full_path_to_genefile = join(this_dir, 'gene_files', genefile)
	if not os.path.isfile(full_path_to_xml):
		print "XML ISN'T FILE"
		return 1
	if not os.path.isfile(full_path_to_genefile):
		print "GENEFILE ISN'T FILE"
		return 1
	
	perl_call = "perl " + join(this_dir, 'parse_xtandem_lobel.pl') + ' '+\
		full_path_to_xml + ' ' + str(threshold) + ' ' + str(label_mass_int) + ' ' +\
		full_path_to_genefile
	print perl_call
	# a = os.system(perl_call)
	pass

# parse_xtandem("/Users/samlobel/String", 1, 300, "RAT75_PTGN.txt")

