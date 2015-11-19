#!/bin/bash
#$ -cwd

module load python/2.7

#python combine.py DES1600_iTRAQ GPM22200014577-DES1600_iTRAQ.xml 1 20 iTRAQ8 1000 2
combinewith_mgf_select.py DESHumanBrainAndCSFreporter_cal GPM22200017692_DESHumanBrainAndCSF.xml 1 10 iTRAQ8 1000 2
#combinewith_mgf_select.py reporter_cal_20ppm GPM22200017257-phosphotransferase.xml 1 10 TMT6 1000 1
combinewith_mgf_select.py DEShumanBrainAndCSFSelected_not_cal GPM22200017692_DESHumanBrainAndCSF_forNonCalMGF.xml 1 20 iTRAQ8 1000 2
#combinewith_mgf_select.py MS3542selectedcal20mgf DES_MS3542_GPM22200017757.xml 1 10 TMT6 1000 1
combinewith_mgf_select.py Test_VLS8972-2notcalnotslelected GPM22200017806searchnotcalnotselected.xml 1 10 TMT6 1000 1
combinewith_mgf_select.py  Test_VLS8972-2notcalSelected GPM22200017807searchSelectedNotCal.xml  1 10 TMT6 1000 1
combinewith_mgf_select.py  Test_VLS8972-2SelectedANDcalibrated GPM22200017808SearchSetectedANDcalibrated.xml  1 10 TMT6 1000 1

combinewith_mgf_select.py  Test_VLS8972-2SelectedANDcalibratedwith20ppm GPM22200017808SearchSetectedANDcalibratedV2.xml  1 20 TMT6 1000 1

combinewith_mgf_select.py  Test_VLS8972-2SelectedNotCalibrated GPM22200018704.xml  1 20 TMT6 1000 1

combinewith_mgf_select.py DES1600mgfSelectedCal20 GPM22200018704.xml 2 20 iTRAQ8 1000 2
combinewithout_mgf_select.py DES1600mgfSelectedCal20 GPM22200018704_secondround.xml 1 20 iTRAQ8 1000 2

combinewith_mgf_select.py DES1600SingleLabel_reporter_cal GPM22200018713.xml 1 20 iTRAQ8 1000 2

combinewith_mgf_select.py DES1600original_reporter_cal GPM22200018704_thirdround.xml 1 20 iTRAQ8 1000 2
DES1600original_reporter_cal

first round of analysis of GPM22200018704 (search without spectrum synthesis, default mods except -nt, -k, +y iTRAQ third refinement round) used 2 for pepide selection (expectation = .01).  
Second round used  1 for peptide selection (expectation =.1) but (I think) used recalibrated mgf files created in first round.
Third round was same as second round but used original reporter cal files.

Do another GPM search ( GPM22200019003) using spectrum synthesis, otherwise identical to above.
Do fenyo procedure without mgselect, using selected, recalibrated mgf files created in third round.
combinewithout_mgf_select.py DES1600original_reporter_cal GPM22200019003.xml 1 20 iTRAQ8 1000 2

combinewithout_mgf_select.py MS3545mgf Phosphtransferase_unlabeledGPM22200019019.xml 1 10 iTRAQ8 0 0


combinewithout_mgf_select.py DES1600mgfSelectedCal20 GPM22200019360.xml 1 20 iTRAQ8 1000 2
combinewith_mgf_select.py DES1500reporter_cal20mgf DES1500GPM22200019633.xml 1 20 TMT6 2000 2
combinewith_mgf_select.py DES1645reporter_cal DES1645_GPM22200020013.xml 1 20 iTRAQ8 1000 2
combinewith_mgf_select.py DES1646reporter_cal DES1646_GPM22200020471.xml 1 20 iTRAQ8 1000 2
combinewith_mgf_select.py TestMgfFiles GPM22200020480.xml 1 20 iTRAQ8 1000 2


From the command line, navigate to DATA directory that contains the folder containing mgf files
(in DATA it is called TestMGFfiles) as well as the GPM....xml output file.
, enter the following:

DATA
-TestMgfFiles
--VLS1.mgf
--VLS2.mgf
-GPM...xml




python ..\CODE\combinewith_mgf_select.py TestMgfFiles GPM22200020480.xml 1 20 iTRAQ8 1000 2



