from subprocess import run
import sys
import os

index = sys.argv[1]
# index = 1
job_prefix = "LBA_beam_"
# jobname = os.path.join(os.getcwd(),job_prefix+str(index)) #TODO: pick the correct jobname automatically
jobname = job_prefix+str(index)
strCommandLine = 'abaqus cae noGUI=run_job_script.py -- ' + jobname  
run(strCommandLine)
# os.system(strCommandLine)
