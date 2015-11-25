import os
from time import time

# a = os.system('perl ./sam_test_perl_exit.pl')
# print a

# Moral of the story, I can print out the exit number. Note that it prints out 256
# times the number, but all I really care about is that it prints something that
# isn't zero.

perl_call = 'perl /Users/samlobel/Code/DAD/Lobel_GUI/SCRIPTS_FOR_GUI/mgf_select_only_one.pl'+\
	' /Users/samlobel/Code/DAD/Lobel_GUI/DATA_TMT10test/TESTmgffiles10/QE00643T.mgf '+\
	'/Users/samlobel/Code/DAD/Lobel_GUI/DATA_TMT10test/TESTmgffiles10/WRITTEN_QE00643T.mgf ' +\
	'20 TMT10 1000 2'
print perl_call

t_1 = time()
# a = os.system('perl /Users/samlobel/Code/DAD/Lobel_GUI/DATA_TMT10test/TESTmgffiles10/')
a = os.system(perl_call)

print a

print "TIME: " + str(time() - t_1)