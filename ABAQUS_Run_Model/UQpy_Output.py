from subprocess import run
import sys
import os

index = sys.argv[1]
#index = 1

job_prefix = "LBA_beam_"
jobname = os.path.join(os.getcwd(),job_prefix+str(index)) #TODO: pick the correct jobname automatically
jobname = jobname + ' ' + str(index)
#jobname = job_prefix+str(index)+".odb "+str(index)

print("Jobname:")
print(jobname)

scriptname = os.path.join(os.getcwd(),"processOdb.py")

strCommandLine = "abaqus python "+ scriptname +" -- " + jobname

print("Run command:")
print(strCommandLine)

#run(strCommandLine)
os.system(strCommandLine)

# from odbAccess import *
#
# # index = sys.argv[1]
# index = 1
# job_prefix = "LBA_beam_"
# # jobname = os.path.join(os.getcwd(),job_prefix+str(index)) #TODO: pick the correct jobname automatically
# jobname = job_prefix+str(index)+'.odb'
#
# a1 = openOdb(jobname)
# f1 = a1.steps['buckle'].frames[2].description
# e1 = float(f1[-11:])
# a1.close()
#
# filename = "UQpy_eval_"+str(index)+".txt"
# with open(filename, "w") as f:
#     f.write(e1)
