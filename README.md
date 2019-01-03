# gui_uni
# gui_uni
//place in the same directory:
	gui_uni.py

	gui.conf
		Working Directory,C:/home/projects/gui_uni/hjm
		Executable,opti_fast.exe
		Command file,parameters_opt.in
		Results are in file,report.txt
		
//In the directory C:/home/projects/gui_uni/hjm  (this is example) put
	opti_fast.exe
	
	parameters_opt.in
		Starting date for reading data from historical rates files, 0
		Number of lines/days to read from historical rates files from starting date,252
		0 - for single curve; 1 - for dual curves,0,1
		Number of days in year - convention,252
		Confidence level,0.99
		Number of Monte Carlo scenarios,1000
		Penalty weight for constraints inclusion into the object function,10
		File name for historical rates of currency A,gbp_2001_2018.in
		File name with initial values of x and constraints for x,hjm_A.in
		File name for historical rates of currency B,eur_2001_2018.in
		File name with initial values of y and ksi with constraints,hjm_B.in
		Nelder-Mead iteration step,1
		The terminating limit for the variance of object function values,0.000001
		Convergence check period,10
		Maximum number of object function evaluation,100
		File name for A output of calibration results,out_data_A.csv
		File name for B output of calibration results,out_data_B.csv
		File name for object function iteration dependence,obj_fn.csv
		File name for calibration summary output,report.txt
		Graphs (0 - no graphs; 1 - make graphs; 2 - make and show graphs),0 ,1,2
		Index of the maturity array for the 3rd output on a graph,2
		1 for calibration; 0 for simulation with given model parameters,1,0
		File results,result

	all othe data files for opti_fast.exe

// run > python gui_uni.py
// the control file "control" is generated:
		 0
		252
		0
		252
		0.99
		1000
		10
		gbp_2001_2018.in
		hjm_A.in
		eur_2001_2018.in
		hjm_B.in
		1
		0.000001
		10
		100
		out_data_A.csv
		out_data_B.csv
		obj_fn.csv
		report.txt
		2
		2
		1
		result
// the program is executed with argument "control":   >> system("opti_fast.exe  control")
	
// result of execution produces few output files including "report.txt" and
	this file (see gui.conf) will be opened in tk text window

	

