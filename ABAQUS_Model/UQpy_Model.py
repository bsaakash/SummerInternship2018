from subprocess import run
import sys
# import os

# index = sys.argv[1]
index = 1
jobname = "C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\LBA_beam_"+str(index)+".inp" #TODO: pick the correct jobname automatically
strCommandLine = 'abaqus cae noGUI=run_job_script.py -- ' + jobname  
run(strCommandLine)
# os.system(strCommandLine)
