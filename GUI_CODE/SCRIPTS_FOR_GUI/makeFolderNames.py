from os.path import join
import os


"""
SelectedMGFSpectra_Min(Field1)(Field2)ions_MinIntensity(Field3)_MassError(Field4)ppm
SelectedReporters_Min(Field1)(Field2)ions_MinIntensity(Field3)_MassError(Field4)ppm
SelectedReporters_Min(Field1)(Field2)ions_MinIntensity(Field3)_InitialMassError(Field4)ppm_RecalMassError(Field5)

Field1=minimum reporters with said intensity
Field2= value from reporter type field
Field3=Minimum Intensity per reporter
Field4=m/z error for initial runthrough
Field5=m/z error for initial runthrough

"""


def construct_selected_mgf_path(form):
	if form['performRecalibration'] == "0":
		a = "MGFSpectraSelected_Min" + str(form['minReporters']) + str(form['reporterIonType']) + "ions" + \
			"_MinIntensity" + str(form['minIntensity']) + "_MassError" + str(form['mzError']) + "ppm"

		full_path = join(form['mgfReadDirPath'], a, '')
		return full_path

	elif form['performRecalibration'] == "1":
		a = "MGFSpectraSelected_Min" + str(form['minReporters']) + str(form['reporterIonType']) + "ions" + \
			"_MinIntensity" + str(form['minIntensity']) + "_InitialMassError" + str(form['mzErrorInitialRun']) + \
			"ppm_RecalMassError" + str(form['mzErrorRecalibration']) + "ppm"

		full_path = join(form['mgfReadDirPath'], a, '')
		return full_path

	else:
		raise Exception("Did not catch anything, must be a bad input")


def construct_reporter_folder_path(form):
	if form['performRecalibration'] == "0":
		a = "ReportersSelected_Min" + str(form['minReporters']) + str(form['reporterIonType']) + "ions" + \
			"_MinIntensity" + str(form['minIntensity']) + "_MassError" + str(form['mzError']) + "ppm"

		full_path = join(form['mgfReadDirPath'], a, '')
		return full_path

	elif form['performRecalibration'] == "1":
		a = "ReportersSelected_Min" + str(form['minReporters']) + str(form['reporterIonType']) + "ions" + \
			"_MinIntensity" + str(form['minIntensity']) + "_InitialMassError" + str(form['mzErrorInitialRun']) + \
			"ppm_RecalMassError" + str(form['mzErrorRecalibration']) + "ppm"

		full_path = join(form['mgfReadDirPath'], a, '')
		return full_path

	else:
		raise Exception("Did not catch anything, must be a bad input")

