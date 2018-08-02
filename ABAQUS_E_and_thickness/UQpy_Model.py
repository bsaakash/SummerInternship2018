from subprocess import run
import sys
import os

index = sys.argv[1]
#index = 1
job_prefix = "LBA_beam_"
# jobname = os.path.join(os.getcwd(),job_prefix+str(index)) #TODO: pick the correct jobname automatically
jobname = job_prefix+str(index)

#strCommandLine = 'abaqus cae noGUI=run_job_script.py -- ' + jobname
scrptnm = os.path.join(os.getcwd(),'run_job_script.py')
#jbnm = os.path.join(os.getcwd(),jobname)
jbnm = jobname

print("Jobname:")
print(jbnm)

#strCommandLine = 'C:\\SIMULIA\\Abaqus\\Commands\\abaqus.bat cae noGUI='+scrptnm+' -- ' + jobname
strCommandLine = 'C:\\SIMULIA\\Abaqus\\Commands\\abaqus.bat cae noGUI='+scrptnm+' -- ' + jbnm
#strCommandLine = 'C:\\SIMULIA\\Abaqus\\6.13-3\\code\\bin\\abq6133.exe cae'

# run(strCommandLine)
os.system(strCommandLine)
