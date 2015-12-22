import utility


def validate_tab_2(form):
	try:
		perform_recalibration = str(request.form['performRecalibration'])
		should_select = str(request.form['mgfOperationToPerform'])
		mgf_read_dir_path = str(request.form['mgfReadDirPath'])
		mgf_file_name = str(request.form['mgfFileName'])
		reporter_type = str(request.form['reporterIonType'])
		min_intensity = str(int(request.form['minIntensity']))
		min_reporters = str(int(request.form['minReporters']))
		mz_error = str(int(request.form['mzError']))

		mz_error_initial_run = str(int(request.form['mzErrorInitialRun']));
		mz_error_recalibration = str(int(request.form['mzErrorRecalibration']));
		




	except:
		return False