from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import sys, os, shutil


# get THIS directory! All of the initial files have got to be relative to this directory!
this_dir = sys.path[0] + "\\"

print this_dir

# Assigns argument values to variables



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
		
print mgfdir + ' ' +xmlfile + ' ' + str(threshold) + ' ' + str(mz_error) + ' ' + type + ' ' + str(min_intensity) + ' ' + str(min_reporters) + ' ' + str(error)
if error==0:
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
	if type=='TMT2':
		start_col=type+'-126'
		end_col=type+'-127'
		label_mass_int=225
	if type=='TMT0':
		start_col=type+'-126'
		end_col=type+'-126'
		label_mass_int=229

	#specify genes text file appropriate for search.  later make part of GUI	
	#genes = pd.read_table(this_dir + 'RAT75_PTGN.txt',header=None,names=['protein','t','g','gene'],index_col=['protein'])
	genes = pd.read_table(this_dir + 'Mus_genes_PTGN.txt',header=None,names=['protein','t','g','gene'],index_col=['protein'])
	#genes = pd.read_table(this_dir + 'H76GRCh38_PTGN.txt',header=None,names=['protein','t','g','gene'],index_col=['protein'])
	genes=genes.drop(['t','g'], axis=1)
	#print genes.loc['ENSRNOP00000000006'][0]
	os.system('perl ' + this_dir + 'parse_xtandem_lobel.pl ' + xmlfile + ' ' + str(threshold) + ' ' + str(int(label_mass_int)))
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
			xml = pd.read_table(xmldir + '/' + filename, index_col=['filename','scan'])
			
			mgf = pd.read_table(mgfdir + '/selected-d' + str(mz_error) + '-' + type + '-' + str(min_intensity) + '-' + str(min_reporters) + '/' + filename, index_col=['filename','scan'])
			dfc=pd.concat([mgf, xml], axis=1)
			dfc_=dfc.dropna()
			dfc_.to_csv(xmldir + '/' + filename + '_nocal_' + str(mz_error) + '_table.txt',sep='\t')

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
				temp=temp.astype(float)
				temp[temp<0]=0
				temp/=sum(temp)
				# This is from the 
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
	with open(xmldir + '_nocal_' + str(mz_error) + '_table.txt', 'w') as outfile:
		for filename in os.listdir(xmldir):
			if filename.endswith('_nocal_' + str(mz_error) + '_table_corrected.txt'):
				with open(xmldir + '/' + filename) as infile:
					for line in infile:
						if (not 'other proteins' in line) or (first==1):
							first=0
							outfile.write(line)



	print "Deleting temporary xml txt file"
	os.remove(xmldir + '.xml.txt')

	print "Deleting temporary XML folder..."
	shutil.rmtree(xmldir)

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
						
						