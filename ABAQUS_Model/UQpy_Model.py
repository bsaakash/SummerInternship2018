from subprocess import run
import sys
# import os

jobname = sys.argv[1]
strCommandLine = 'abaqus cae noGUI=run_job_script.py -- ' + jobname  
run(strCommandLine)
# os.system(strCommandLine)
